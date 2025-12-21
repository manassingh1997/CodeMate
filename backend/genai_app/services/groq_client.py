from groq import Groq
from django.conf import settings

client = Groq(api_key=settings.GROQ_API_KEY)

def call_groq(prompt: str) -> str:
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a DSA mentor."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.4,
    )

    return response.choices[0].message.content