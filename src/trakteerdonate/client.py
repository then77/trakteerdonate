# ############################################
# 
#        Trakteer Donate Client Library
#          ~~ 2023 (c) by Realzzy ~~
# 
# ############################################

# Import os, asyncio, json parser, logger, and traceback modules
import os, asyncio, json, logging, traceback

# Import threading module
from threading import Thread

# Import connection handler modules
import websockets

# Import Data Types
from .data_types import *



# Create Logger
def make_logger():
    log = logging.getLogger("Trakteer")
    log.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    formatter = logging.Formatter(f"[%(name)s %(levelname)s] - %(message)s")
    ch.setFormatter(formatter)
    log.addHandler(ch)
    return log
log = make_logger()



# Make client class
class Client:
    """

    Client to handle Trakteer donation events
    Available methods to override:
    - on_connect(ws): Called when websocket is connected
    - on_close(ws, e): Called when websocket is closed
    - on_error(ws, e): Called when websocket returns error
    - on_donation(data): Called when donation is received
    - on_message(data): Called when raw message received

    2023 (c) by Realzzy
    """

    # Initiate the client
    def __init__(self, userHash = None, streamKey = None, block = True, test = False):

        # Automatically provide user hash and stream key from environment variables if not provided in parameters
        if userHash == None:
            if os.getenv("TRAKTEER_USERHASH") != None: userHash = os.getenv("TRAKTEER_USERHASH")
            else: raise TrakteerMissingUserHash("Missing user hash! Please provide user hash when calling this function or set TRAKTEER_USERHASH environment variable.")

        if streamKey == None:
            if os.getenv("TRAKTEER_STREAMKEY") != None: streamKey = os.getenv("TRAKTEER_STREAMKEY")
            else: raise TrakteerMissingStreamKey("Missing stream key! Please provide stream key when calling this function or set TRAKTEER_STREAMKEY environment variable.")

        # Auto remove "trstream-" from stream key if any
        if streamKey.startswith("trstream-"):
            log.warn("Ignoring 'trstream-' prefix in stream key. Please remove it in the future.")
            streamKey = streamKey[9:]
        
        # Set variables
        self.ws = None
        self.hash = str(userHash)
        self.streamKey = str(streamKey)

        if isinstance(block, bool): self.block = block
        else:
            log.warn("'block' argument is not a boolean! Defaulting to False...")
            self.block = True

        if isinstance(test, bool): self.test = test
        else:
            log.warn("'test' argument is not a boolean! Defaulting to False...")
            self.test = False

        # States for websocket
        self.has_connected = False
        self.subs_succed = False

    # Run client
    def start(self, **kwargs):

        # Connect to the websocket
        def wsconnect(self):
            async def connect(self):
                try:
                    async with websockets.connect(f"wss://socket.trakteer.id/app/2ae25d102cc6cd41100a?protocol=7&client=js&version=5.1.1&flash=false") as ws:
                        self.ws = ws
                        while True:
                            try:
                                data = await ws.recv()
                                #print("From 1 : " + data)
                                await self.__parse_message(data)
                            except websockets.exceptions.ConnectionClosedError as e:
                                await self.__class__.on_close(ws, e)
                                break
                            except BaseException as e:
                                await self.__class__.on_error(ws, e)
                                break
                
                except BaseException as e:
                    message = "Can't connect to websocket"
                    if self.has_connected: message = "Websocket returned error"
                    raise TrakteerWebsocketError(f"{message}:\n{traceback.format_exc()}")
                else:
                    if self.has_connected:
                        log.debug("Reconnecting...")
                        await connect(self)

            asyncio.run(connect(self))

        # Run thread
        if self.block == False: Thread(target=wsconnect, args=[self]).start()
        else: wsconnect(self)

    # First handler after websocket connect (unoverridable)
    async def __connected(self):

        # Send subscribe event for donation
        await self.ws.send(json.dumps({
            "event": "pusher:subscribe",
            "data": {
                "auth": "",
                "channel": f"creator-stream.{self.hash}.trstream-{self.streamKey}"
            }
        }))

        # Send subscribe event for donation test if enabled
        if self.test == True:
            await self.ws.send(json.dumps({
                "event": "pusher:subscribe",
                "data": {
                    "auth": "",
                    "channel": f"creator-stream-test.{self.hash}.trstream-{self.streamKey}"
                }
            }))

        # Run ping every 10 seconds to make sure still connected
        def run_ping(self):
            async def ping(self):
                while True:
                    await asyncio.sleep(10)
                    await self.ws.send(json.dumps({"event": "pusher:ping", "data": {}}))
                    log.debug("Sent ping to websocket")
                    
            asyncio.run(ping(self))

        # Check if subscription succeeded
        async def check_subs():
            if self.subs_succed == True:
                Thread(target=run_ping, args=[self]).start()
                if self.has_connected != True:
                    await self.__class__.on_connect(self.ws)
                    self.has_connected = True
            else:
                await asyncio.sleep(1)
                await check_subs()
        
        Thread(target=asyncio.run, args=[check_subs()]).start()

    # First handler on websocket message (unoverridable)
    async def __parse_message(self, rawdata):
        try:
            data = json.loads(rawdata)
        except json.decoder.JSONDecodeError as e:
            log.warn("Can't parse message received from websocket. Ignoring...")
        else:
            if data["event"] == "pusher:connection_established":
                await self.__connected()
            elif data["event"] == "pusher_internal:subscription_succeeded":
                self.subs_succed = True
            elif "BroadcastNotificationCreated" in data["event"]:
                await self.__class__.on_donation(self.ws, TrakteerDonationData(json.loads(data["data"])))

            await self.__class__.on_message(self.ws, data)

    # Handler when websocket connected (overridable)
    @staticmethod
    async def on_connect(ws):
        pass

    # Handler when websocket received message (overridable)
    @staticmethod
    async def on_message(ws, data):
        pass

    # handler when websocket received donation (overridable)
    @staticmethod
    async def on_donation(ws, data):
        pass

    # Handler when websocket closed (overridable)
    @staticmethod
    async def on_close(ws, e):
        pass

    # Handler when websocket error (overridable)
    @staticmethod
    async def on_error(ws, e):
        pass

    # Method to override function above
    @classmethod
    def event(cls, func):
        if func.__name__ in ["__connected", "__parse_message"]:
            raise TrakteerMethodUnoverridable(f"Method '{func.__name__}' is unoverridable!")
        
        setattr(cls, func.__name__, func)
        return func

        
        
