from trakteerdonate import Client
from time import sleep

client = Client("b9073avgmok3ekzg", "nHosJttAGiUsVj4CfirU", block=False, test=True)

@client.event
async def on_connect(ws):
    print("Connected to Trakteer!")

@client.event
async def on_donation(ws, data):
    print("Received donation:")
    print(f"  - Name: {data.name}")
    print(f"  - Amount: {data.amount}")
    print(f"  - Message: {data.message}")

client.start()
time.sleep(30)