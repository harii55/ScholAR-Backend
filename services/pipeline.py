from datetime import datetime, timezone as UTC
from services.ocr import run_ocr
from services.stt import run_stt
from services.llm import query_llm
import json

async def create_learning_response(image_path: str, audio_path: str):
    ocr_text = await run_ocr(image_path)
    stt_text = await run_stt(audio_path)

    input_data = {
        "ocr_text": ocr_text,
        "stt_text": stt_text
    }

    prompt = json.dumps(input_data)

    output = await query_llm(prompt)

    return {
        "input_data": input_data,
        "output_data": output
    }
