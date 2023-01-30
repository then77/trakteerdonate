<p align="center"><b>⚠️ NOTE: THIS PROJECT IS ONLY FOR EDUCATIONAL PURPOSE!! ⚠️<br>I WONT RESPONSIBLE FOR SOMETHING HAPPEN WHEN USING THIS PROGRAM!!</b></p>

<h1 align="center"><img src="https://raw.githubusercontent.com/then77/trakteerdonate/main/trakteerdonate.png" alt="Trakteer Donate"></h1>
<p align="center">An easy way to listen for Trakteer donation in Python</p>

## Installation
To install this package, you can easily use pip!
```bash
pip install trakteerdonate
```

Or,

```bash
pip install git+https://github.com/then77/trakteerdonate
```

## Package Usage
1. First open your **Trakteer** and go to **Stream Overlay** ([here](https://trakteer.id/manage/stream-settings))
2. On the **Widget URL**, copy the key, and the hash
3. Create a code and import the `Client` function.
```python
from trakteerdonate import Client
client = Client("hash", "streamKey")
# Replace "hash" and "streamKey" with the key you copied before
```
4. Add listener for donation
```python
@client.event
async def on_donation(ws, data):
    print("Received donation:")
    print(f"  - Name: {data.name}")
    print(f"  - Amount: {data.amount}")
    print(f"  - Message: {data.message}")
```
5. Last, add this code **To the bottom of the code** and run!
```python
client.start()
```

The reason it should be placed on the bottom because its a blocking function.

## Example Code
```python
from trakteerdonate import Client

client = Client("hash", "streamKey")

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
```

## More Info For API
*Wait, do you have another API to interact instead of only listening donation?*

Currenly no since i dont have much time to do that. But, i found another cool project that can do something like that [here](https://github.com/KatowProject/trakteer-scraper). Even though it uses **Javascript**, its still awesome.

## Known Issue
Since this package use websocket to communicate, some host like [`Replit`](https://replit.com/talk/ask/Socket-not-connecting/52103) may not allow this protocol. But, you still can run on your local pc or another host that support it, or you can use alternative library i mentioned above since it doesn't use websocket thing.

## Repository License
This repository and its code is under the MIT License. [Read more here](https://github.com/then77/trakteerdonate/blob/main/LICENSE).
