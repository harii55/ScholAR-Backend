import asyncio
import os
from datetime import datetime,UTC
import wave

AUDIO_SAVE_PATH = "static/audio"
os.makedirs(AUDIO_SAVE_PATH, exist_ok=True)

async def handle_audio_stream(websocket):
    buffer = bytearray()
    last_chunk_time = datetime.now(UTC)
    filename = f"{datetime.now(UTC).timestamp()}.wav"
    file_path = os.path.join(AUDIO_SAVE_PATH, filename)

    while True:
        try:
            data = await asyncio.wait_for(websocket.receive_bytes(), timeout=5.0)
            buffer.extend(data)
            last_chunk_time = datetime.now(UTC)    
        except asyncio.TimeoutError:
            print("Silence detected (5s timeout). Closing stream.")
            break

    # Save as .wav
    with wave.open(file_path, 'wb') as wav_file:
        wav_file.setnchannels(1)            # Mono
        wav_file.setsampwidth(2)            # 16-bit audio
        wav_file.setframerate(16000)        # 16KHz sample rate
        wav_file.writeframes(buffer)

    print(f"Saved audio to: {file_path}")
