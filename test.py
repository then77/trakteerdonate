from trakteerdonate import Client

client = Client("b9073avgmok3ekzg", "trstream-nHosJttAGiUsVj4CfirU", test = True)

@client.event
async def on_connect(ws):
    print("Connected!")

@client.event
async def on_donation(ws, data):
    print(f"\n\nReceived: {data.to_dict()}\n\n")
    print(f"Name: {data.name}\nMessage: {data.message}")

client.start()