from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel

from reviewer import ask_llm

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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

    filename = f"../reports/review_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write("CODE:\n")
        f.write(request.code)
        f.write("\n\n")
        f.write("AI REVIEW:\n")
        f.write(response)

    return {
        "response": response
    }