import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from api.image_upload import router as upload_router
from api.audio_stream import router as stream_router

app = FastAPI(
    title="ScholAR Backend V0",
    description="Backend for ScholAR Smart Glasses",
    version="0.1"
)
os.makedirs("static/images", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(upload_router, prefix="/upload")
app.include_router(stream_router)