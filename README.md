<p align="center"><b>⚠️ NOTE: THIS PROJECT IS ONLY FOR EDUCATIONAL PURPOSE!! ⚠️<br>I WONT RESPONSIBLE FOR SOMETHING HAPPEN WHEN USING THIS PROGRAM!!</b></p>

<h1 align="center">Trakteer Donate</h1>
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

## Repository License
This repository and its code is under the MIT License. [Read more here](https://github.com/then77/trakteerdonate/blob/main/LICENSE).
