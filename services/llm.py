import os
import openai


client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
async def query_llm(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-5",  # or your model
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
