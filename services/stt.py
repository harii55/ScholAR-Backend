from google.cloud import speech
import io

async def run_stt(audio_path: str) -> str:
    client = speech.SpeechClient()

    with io.open(audio_path, 'rb') as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    response = client.recognize(config=config, audio=audio)

    result = ""
    for r in response.results:
        result += r.alternatives[0].transcript + " "

    return result.strip()
