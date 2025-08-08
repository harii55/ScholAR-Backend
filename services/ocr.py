from google.cloud import vision
import io
import os
from dotenv import load_dotenv

load_dotenv(override=True)

google_application_credentials = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
print("GOOGLE_APPLICATION_CREDENTIALS:", google_application_credentials)

async def run_ocr(image_path: str) -> str:
    client = vision.ImageAnnotatorClient()

    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.document_text_detection(image=image)

    if response.error.message:
        raise Exception(f"OCR API error: {response.error.message}")

    return response.full_text_annotation.text
