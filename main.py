import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from api.image_upload import router as upload_router
from api.audio_stream import router as stream_router
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from api.android_stream import router as android_ws_router

load_dotenv(override=True)

app = FastAPI(
    title="ScholAR Backend V0",
    description="Backend for ScholAR Smart Glasses",
    version="0.1"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

os.makedirs("static/images", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(upload_router, prefix="/upload")
app.include_router(stream_router, prefix="/stream")
app.include_router(android_ws_router, prefix="/ws")
