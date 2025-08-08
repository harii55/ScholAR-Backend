# utils/file_utils.py
import os
from datetime import datetime
from fastapi import UploadFile

SAVE_DIR = "static/images"

async def save_uploaded_image(file: UploadFile) -> str:
    os.makedirs(SAVE_DIR, exist_ok=True)
    filename = f"{datetime.utcnow().timestamp()}_{file.filename}"
    file_path = os.path.join(SAVE_DIR, filename)
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)
    return os.path.normpath(file_path)
