# 🤖 LinkedIn Post Generator — AI Agent
### Module 20 Assignment | LangChain + Google Gemini

---

## 📌 Project Overview
An AI Agent built with LangChain that generates professional LinkedIn posts based on:
- **Topic** (e.g. "AI in Healthcare", "Remote Work Productivity")
- **Language** (English, Bengali, Spanish, French, Arabic, Hindi, Portuguese, German, Mandarin)
- **Tone** (Professional, Inspirational, Storytelling, Data-driven, Conversational, Thought Leader)

---

## 🧠 Tech Stack
- Python
- Flask
- LangChain
- Google Gemini API

---

## 📁 Project Structure

---

linkedin_agent/

├── agent.py          # LangChain Agent core logic

├── app.py            # Flask web application

├── requirements.txt  # Python dependencies

├── README.md         # Project documentation

├── templates/

│   └── index.html    # Web UI

└── static/

├── css/style.css

└── js/main.js


## 🚀 How to Run

### 1. Install dependencies
```bash
pip install langchain langchain-google-genai google-generativeai flask
```

### 2. Add your API Key
Open `app.py` and add your Gemini API key:
```python
API_KEY = os.getenv("GEMINI_API_KEY", "your-gemini-api-key-here")
```

### 3. Run the app
```bash
python app.py
```

### 4. Open browser

http://localhost:5000

---

## ✅ Features
- LangChain Agent with ChatPromptTemplate
- 9 supported languages including Bengali
- 6 tone options
- Flask REST API
- LinkedIn-style post preview UI
- Copy to clipboard & Regenerate

---

## 👨‍💻 Module 20 Assignment
**Course**: AI Agents with LangChain  
**Student**: ASHIQ RAHMAN CHOWHDURY