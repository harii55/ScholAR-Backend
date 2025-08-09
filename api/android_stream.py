from fastapi import APIRouter, WebSocket, WebSocketDisconnect

router = APIRouter()

connected_clients = set()

@router.websocket("/android")
async def websocket_stream(websocket: WebSocket):
    await websocket.accept()
    connected_clients.add(websocket)
    try:
        while True:
            await websocket.receive_text()  # keep connection alive; no input needed
    except WebSocketDisconnect:
        connected_clients.remove(websocket)
