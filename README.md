# 🤖 LLM Code Review Assistant

An AI-powered code review assistant built using FastAPI, Ollama, and Qwen 3B.

The application analyzes source code and provides:

- Code Summary
- Issues Found
- Security Concerns
- Improvement Suggestions
- Downloadable Review Reports

---

## 🚀 Features

- AI-powered code review using Qwen 3B
- FastAPI backend
- REST API integration
- Modern dark-themed frontend
- Automatic issue detection
- Security recommendations
- Downloadable review reports
- Local LLM execution using Ollama

---

## 🛠 Tech Stack

### Backend
- Python
- FastAPI
- Uvicorn
- Requests

### AI Model
- Ollama
- Qwen3:8B

### Frontend
- HTML
- CSS
- JavaScript

---

## 📂 Project Structure

```text
LLM-code-review-assistant/
│
├── backend/
│   ├── app.py
│   └── reviewer.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── screenshots/
│   ├── home.png
│   └── review.png
│
├── reports/
│
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/pavan19-06/LLM-code-review-assistant.git
cd LLM-code-review-assistant
```

### Install Dependencies

```bash
pip install fastapi uvicorn requests
```

### Install Ollama

Download and install Ollama:

https://ollama.com

Pull Qwen Model:

```bash
ollama pull qwen3:8b
```

---

## ▶️ Run Backend

```bash
cd backend
uvicorn app:app --reload
```

Backend runs at:

```text
http://127.0.0.1:8000
```

---

## 🌐 Run Frontend

Open:

```text
frontend/index.html
```

in your browser.

---

## 📸 Screenshots

### Home Interface

![Home UI](screenshot/ui-dashboard.png)

---

## 📝 Example Workflow

1. Paste source code into the input area
2. Click **Review Code**
3. Code is sent to FastAPI backend
4. Ollama analyzes the code using Qwen
5. Review is displayed on screen
6. Download report if needed

---

## 🎯 Future Improvements

- Multiple language support
- Syntax highlighting
- Authentication system
- Streamlit deployment
- Docker support
- Cloud-hosted inference

---

## 👨‍💻 Author

**Pavan R**

B.Tech AIML Student

Built as a hands-on AI + FastAPI + Ollama project to learn local LLM integration and software engineering workflows.

---

## ⭐ If you like this project

Give the repository a star on GitHub ⭐
