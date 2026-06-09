from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "LLM Code Review Assistant Running"
    }