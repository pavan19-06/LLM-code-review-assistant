import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def ask_llm(prompt):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "qwen3:8b",
            "prompt": f"""
You are a senior software engineer.

Review the following code and provide:

1. Summary
2. Issues Found
3. Suggestions for Improvement

Code:
{prompt}
""",
            "stream": False
        }
    )

    return response.json()["response"]