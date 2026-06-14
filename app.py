from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

app = Flask(__name__)

# 🔑 Gemini client (NEW SDK)
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


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

    def __init__(self, client):
        self.client = client

    def generate(self, topic, language="English", tone="Professional"):

        prompt = f"""
You are a professional LinkedIn post writer.

CRITICAL RULE:
Write ONLY in {language}.
Do NOT use any other language.

Topic: {topic}
Tone: {tone}

Requirements:
- 150–250 words
- 2–4 paragraphs
- Add hashtags at the end
- Professional LinkedIn style

Return ONLY the post.
"""

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return {
            "post": response.text,
            "topic": topic,
            "language": language,
            "tone": tone
        }


# 🤖 Agent init
agent = LinkedInPostAgent(client)


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

    topic = data.get("topic", "").strip()
    language = data.get("language", "English")
    tone = data.get("tone", "Professional")

    if not topic:
        return jsonify({"error": "Topic is required"}), 400

    try:
        result = agent.generate(topic, language, tone)
        return jsonify(result)

    except Exception as e:
        print("ERROR:", str(e))
        return jsonify({
            "error": "Generation failed",
            "detail": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)