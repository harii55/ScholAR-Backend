from api.android_stream import connected_clients

async def send_response_to_android(text: str, tts_url: str):
    data = {
        "type": "response",
        "text": text,
        "tts_url": tts_url,
    }
    remove = []
    for client in connected_clients:
        try:
            await client.send_json(data)
        except Exception:
            remove.append(client)
    for r in remove:
        connected_clients.remove(r)
