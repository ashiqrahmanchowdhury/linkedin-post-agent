# 🤖 LinkedIn Post Generator — AI Agent
### Module 20 Assignment | LangChain + Google Gemini

---

## 📌 Project Overview
An AI-powered agent that generates professional LinkedIn posts based on user input.

Users can control:
- Topic (e.g. "AI in Healthcare", "Remote Work Productivity")
- Language (English, Bengali, Spanish, French, Arabic, Hindi, Portuguese, German, Mandarin)
- Tone (Professional, Inspirational, Storytelling, Data-driven, Conversational, Thought Leader)

---

## 🧠 Tech Stack
- Python
- Flask
- LangChain
- Google Gemini API

---

## 📁 Project Structure
linkedin_agent/
│── agent.py
│── app.py
│── requirements.txt
│── README.md
│── templates/
│   └── index.html
└── static/
    ├── css/style.css
    └── js/main.js

---

## 🚀 How to Run

### 1. Install dependencies
pip install langchain langchain-google-genai google-genai flask python-dotenv

---

### 2. Add API Key
Create a .env file:
GEMINI_API_KEY=your-gemini-api-key

---

### 3. Run project
python app.py

---

### 4. Open browser
http://localhost:5000

---

## ✨ Features
- AI-powered LinkedIn post generation
- Multi-language support (9 languages)
- Multiple tone selection
- Flask REST API
- Modern UI (HTML + CSS + JS)
- Copy & regenerate functionality

---

## 🧠 Workflow
User Input → Flask API → Gemini AI → Prompt Engineering → LinkedIn Post Output

---

## 👨‍💻 Module 20 Assignment
Course: AI Agents with LangChain  
Student: ASHIQ RAHMAN CHOWDHURY

---

## 📌 Notes
- Uses latest Gemini API
- Keep API key secure (.env file)
- Do not upload secrets to GitHub

---

## ⭐ Future Improvements
- LinkedIn auto-posting system
- Post scheduling feature
- Analytics dashboard
- Advanced prompt optimization