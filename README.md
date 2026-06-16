# 🤖 LLM Code Review Assistant

An AI-powered code review assistant built using FastAPI and Ollama.

## 🚀 Features

- AI-powered code review using Qwen
- FastAPI backend
- REST API endpoint (`/review`)
- Automatic code analysis
- Timestamped report generation
- Reports saved locally in `.txt` format

## 📁 Project Structure

```
llm-code-review-assistant/
│
├── backend/
│   ├── main.py
│   └── reviewer.py
│
├── reports/
│   └── review_*.txt
│
├── docs/
├── frontend/
├── .gitignore
└── README.md
```

## 🛠️ Tech Stack

- Python
- FastAPI
- Ollama
- Qwen
- Uvicorn

## ▶️ Run the Project

```bash
cd backend
uvicorn main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

## ✅ Current Progress

- ✅ Week 1 - FastAPI + Ollama Integration
- ✅ Week 2 - Review API Endpoint
- ✅ Week 3 - Automatic Report Generation

## 📌 Upcoming

- Week 4 - Frontend UI
- Week 5 - File Upload Support
- Week 6 - Final Polish & Deployment
