from datetime import datetime, timezone as UTC
from services.ocr import run_ocr
from services.stt import run_stt
from services.llm import query_llm
async def create_learning_response(image_path: str, audio_path: str):
    ocr_text = await run_ocr(image_path)
    stt_text = await run_stt(audio_path)

    prompt = f"""
You are ScholAR, an intelligent AI tutor built into a pair of smart glasses for students.

Your job is to help the student understand what they are looking at and asking about, using the visual context from an image and the question they asked by voice.

Be clear, concise, and educational. Prioritize short, easy-to-understand answers. You can include definitions, explanations, or step-by-step reasoning if needed.

---

Visual Context (text detected in the image):
{ocr_text}

Audio Context (spoken statements from the user):
{stt_text}

---

Respond in a helpful, teacher-like tone.
"""

    answer = await query_llm(prompt)

    return {
        "ocr": ocr_text,
        "stt": stt_text,
        "answer": answer
    }
