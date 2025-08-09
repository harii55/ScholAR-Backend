import os
from google.cloud import texttospeech
from datetime import datetime

os.makedirs("static/tts", exist_ok=True)

async def generate_tts(text: str) -> str:
    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text=text)

    # Select the voice parameters
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL,
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    filename = f"tts_{int(datetime.utcnow().timestamp())}.mp3"
    filepath = os.path.join("static/tts", filename)

    with open(filepath, "wb") as out:
        out.write(response.audio_content)

    return f"/tts/{filename}"
