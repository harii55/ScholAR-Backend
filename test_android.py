import asyncio
import websockets

async def listen():
    uri = "ws://localhost:8000/ws/android"
    async with websockets.connect(uri) as ws:
        while True:
            msg = await ws.recv()
            print("Received:", msg)

asyncio.run(listen())
