from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from services.audio_handler import handle_audio_stream
from services.session import get_latest_image
from services.pipeline import create_learning_response

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
                print("LLM Response:", response["answer"])

                # TODO: send response to Android WS
                
            else:
                print("No image available — skipping pipeline.")
        else:
            print("No audio recorded — skipping pipeline.")
    
    except WebSocketDisconnect:
        print("Client disconnected during audio stream.")
    finally:
        print("connection closed")
