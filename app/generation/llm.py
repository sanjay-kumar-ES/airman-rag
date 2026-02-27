import requests
from app.config import LLM_MODEL


OLLAMA_URL = "http://localhost:11434/api/generate"


def generate_answer(prompt):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": LLM_MODEL,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.2
            }
        }
    )

    result = response.json()
    return result["response"].strip()