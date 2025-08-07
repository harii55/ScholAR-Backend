from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from services.audio_handler import handle_audio_stream

router = APIRouter()

@router.websocket("/stream/audio")
async def stream_audio(websocket: WebSocket):
    await websocket.accept()
    print("connection open")
    try:
        await handle_audio_stream(websocket)
    except WebSocketDisconnect:
        print("Client disconnected during audio stream.")
    finally:
        print("connection closed")