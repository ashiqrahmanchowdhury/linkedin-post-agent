from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()

app = Flask(__name__)

print("GEMINI KEY:", os.getenv("GEMINI_API_KEY"))


class LinkedInPostAgent:

    SUPPORTED_LANGUAGES = [
        "English", "Bengali", "Spanish", "French",
        "Arabic", "Hindi", "Portuguese"
    ]

    SUPPORTED_TONES = [
        "Professional",
        "Inspirational",
        "Storytelling",
        "Conversational"
    ]

    def __init__(self, model):
        self.model = model

    def generate(self, topic, language="English", tone="Professional"):

        prompt = f"""
Write a LinkedIn post.

CRITICAL RULE:
Write ONLY in {language}. Do not use English.

Topic: {topic}
Tone: {tone}

- 150–250 words
- 2–4 paragraphs
- hashtags at end
"""

        response = self.model.generate_content(prompt)

        return {
            "post": response.text,
            "topic": topic,
            "language": language,
            "tone": tone
        }


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-2.5-flash")

agent = LinkedInPostAgent(model)


@app.route("/")
def index():
    return render_template(
        "index.html",
        languages=LinkedInPostAgent.SUPPORTED_LANGUAGES,
        tones=LinkedInPostAgent.SUPPORTED_TONES,
    )


@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()

    topic = data.get("topic", "")
    language = data.get("language", "English")
    tone = data.get("tone", "Professional")

    print("LANG:", language)

    try:
        result = agent.generate(topic, language, tone)
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)