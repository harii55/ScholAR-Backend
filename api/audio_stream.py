import json
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from services.audio_handler import handle_audio_stream
from services.session import get_latest_image
from services.pipeline import create_learning_response
from services.tts import generate_tts
from utils.broadcast_utils import send_response_to_android
router = APIRouter()

@router.websocket("/audio")
async def stream_audio(websocket: WebSocket):
    await websocket.accept()
    print("connection open")
    try:
        audio_path = await handle_audio_stream(websocket)

        if audio_path:
            image_path = get_latest_image()
            if image_path:
                print(f"Triggering LLM pipeline with image: {image_path} and audio: {audio_path}")
                response = await create_learning_response(image_path, audio_path)
                llm_json = json.loads(response["output_data"])
                explanation = llm_json.get("explanation", "")

                print("LLM's Explanation:", explanation)
                print("LLM full response:", response)
                tts_url = await generate_tts(explanation)

                # Send to Android clients
                await send_response_to_android(llm_json, tts_url)
                
            else:
                print("No image available — skipping pipeline.")
        else:
            print("No audio recorded — skipping pipeline.")
    
    except WebSocketDisconnect:
        print("Client disconnected during audio stream.")
    finally:
        print("connection closed")
