import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is missing from .env")

client = Groq(api_key=GROQ_API_KEY)

MODEL = "openai/gpt-oss-20b"


def get_llm_response(messages):
    """
    Send conversation messages to GPT-OSS 20B through Groq.
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0.2,
        max_tokens=1000
    )

    return response.choices[0].message.content