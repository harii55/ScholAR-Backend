# api/upload.py
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from utils.file_utils import save_uploaded_image
from services.session import set_latest_image
router = APIRouter()

@router.post("/image")
async def upload_image(file: UploadFile = File(...)):
    saved_path = await save_uploaded_image(file)
    set_latest_image(saved_path)
    return JSONResponse(content={"status": "success", "image_path": saved_path})
