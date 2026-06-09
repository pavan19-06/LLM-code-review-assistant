import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def ask_llm(prompt):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "qwen3:8b",
            "prompt": f"Answer directly. Do not show thinking process.\n\n{prompt}",
            "stream": False
        }
    )

    return response.json()["response"]