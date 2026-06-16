from fastapi import FastAPI
from pydantic import BaseModel

from reviewer import ask_llm

app = FastAPI()

class CodeReviewRequest(BaseModel):
    code: str

@app.get("/")
def home():
    return {
        "message": "LLM Code Review Assistant Running"
    }

@app.post("/review")
def review(request: CodeReviewRequest):
    response = ask_llm(request.code)

    return {
        "response": response
    }