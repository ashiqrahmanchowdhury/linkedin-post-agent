from google import genai
import os

class LinkedInPostAgent:
    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)

    def generate(self, topic, language="English", tone="Professional"):

        LANG_MAP = {
            "Bengali": "Bangla",
            "Hindi": "Hindi",
            "English": "English",
            "Spanish": "Spanish",
            "French": "French",
            "Arabic": "Arabic",
            "Portuguese": "Portuguese"
        }

        lang = LANG_MAP.get(language, language)

        prompt = f"""
You are a multilingual LinkedIn writer.

WRITE RULE:
You MUST respond ONLY in this language: {language}

Do not use English at all.
Even single English word is NOT allowed.

Topic: {topic}
Tone: {tone}

Format:
- 150–250 words
- 2–4 paragraphs
- hashtags at end

Return ONLY post.
"""

        response = self.client.models.generate_content(
            model="models/gemini-2.5-flash",
            contents=prompt
        )

        post = response.text.strip()

        def is_mostly_english(text):
            english_chars = sum(c.isascii() for c in text)
            return english_chars / max(len(text), 1) > 0.7

        if language != "English" and is_mostly_english(post):
            response = self.client.models.generate_content(
                model="models/gemini-2.5-flash",
                contents=prompt + "\nIMPORTANT: LAST RESPONSE WAS WRONG. FIX LANGUAGE."
            )
            post = response.text.strip()

        return {
            "post": post,
            "topic": topic,
            "language": language,
            "tone": tone
        }