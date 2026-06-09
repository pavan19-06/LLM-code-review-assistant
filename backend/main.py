from fastapi import FastAPI
from pydantic import BaseModel

from reviewer import ask_llm

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.get("/")
def home():
    return {
        "message": "LLM Code Review Assistant Running"
    }

@app.post("/ask")
def ask(request: PromptRequest):
    response = ask_llm(request.prompt)

    return {
        "response": response
    }