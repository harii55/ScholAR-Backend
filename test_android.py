import asyncio
import websockets

async def listen():
    uri = "ws://localhost:8000/ws/android"
    while True:
        try:
            async with websockets.connect(uri, ping_timeout=60) as ws:
                while True:
                    msg = await ws.recv()
                    print(msg)
        except Exception as e:
            print(f"Disconnected: {e}. Reconnecting in 5 seconds...")
            await asyncio.sleep(5)

asyncio.run(listen())
