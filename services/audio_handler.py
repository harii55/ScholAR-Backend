import asyncio
import os
from datetime import datetime, UTC
import wave
from services.pipeline import create_learning_response
from services.session import get_latest_image


AUDIO_SAVE_PATH = "static/audio"
os.makedirs(AUDIO_SAVE_PATH, exist_ok=True)

async def handle_audio_stream(websocket):
    buffer = bytearray()
    last_chunk_time = datetime.now(UTC)
    filename = f"{datetime.now(UTC).timestamp()}.wav"
    file_path = os.path.join(AUDIO_SAVE_PATH, filename)
    file_path = os.path.normpath(file_path)
    
    total_bytes = 0
    while True:
        try:
            data = await asyncio.wait_for(websocket.receive_bytes(), timeout=5.0)
            buffer.extend(data)
            total_bytes += len(data)
            print(f"Received {len(data)} bytes, total: {total_bytes} bytes")
            last_chunk_time = datetime.now(UTC)    
        except asyncio.TimeoutError:
            print("Silence detected (5s timeout). Closing stream.")
            break
        except Exception as e:
            if str(e).startswith("(1000"):
                print("Client closed connection cleanly (1000)")
            else:
                print(f"Error receiving data: {e}")
            break


    if buffer:
        with wave.open(file_path, 'wb') as wav_file:
            wav_file.setnchannels(1)            # Mono
            wav_file.setsampwidth(2)            # 16-bit audio
            wav_file.setframerate(16000)        # 16KHz sample rate
            wav_file.writeframes(buffer)
        print(f"Saved audio to: {file_path} ({len(buffer)} bytes)")
        return file_path
    else:
        print("No audio data received, nothing saved.")
        return None 
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    #     image_path = get_latest_image()

    #     if image_path:
    #         print(f"Triggering LLM pipeline with image: {image_path} and audio: {file_path}")
    #         response = await create_learning_response(image_path, file_path)
    #         return response
    #     else:
    #         print("No image found. Skipping trigger.")
    #     return None
    # else:
    #     print("No audio data received, nothing saved.")
    #     return None
    