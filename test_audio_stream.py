# test_audio_stream.py

import asyncio
import websockets
import wave

AUDIO_FILE = "output.wav"  # Must be 16-bit PCM, mono, 16KHz

async def stream_audio():
    uri = "ws://localhost:8000/stream/audio"
    

    async with websockets.connect(uri) as websocket:
        with wave.open(AUDIO_FILE, 'rb') as wf:
            assert wf.getframerate() == 16000
            assert wf.getsampwidth() == 2
            assert wf.getnchannels() == 1

            chunk = 1024
            data = wf.readframes(chunk)

            while data:
                await websocket.send(data)
                await asyncio.sleep(chunk / 16000 / 2)  # Approx delay based on sample rate
                data = wf.readframes(chunk)

        print("Audio streaming complete.")

asyncio.run(stream_audio())
