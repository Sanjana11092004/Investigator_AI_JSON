import json

from groq import Groq

from src.config.settings import settings


class GroqService:

    def __init__(self):

        self.client = Groq(
            api_key=settings.GROQ_API_KEY
        )

    def extract_clinical_json(
        self,
        text: str,
        prompt: str
    ) -> dict:

        response = (
            self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                temperature=0,
                messages=[
                    {
                        "role": "system",
                        "content": prompt
                    },
                    {
                        "role": "user",
                        "content": text
                    }
                ]
            )
        )

        content = (
            response
            .choices[0]
            .message
            .content
            .strip()
        )

        if content.startswith("```"):

            content = (
                content
                .replace("```json", "")
                .replace("```", "")
                .strip()
            )

        try:

            return json.loads(content)

        except Exception as e:

            return {
                "error": str(e),
                "raw_response": content
            }

    def generate(
        self,
        prompt: str
    ) -> str:

        response = (
            self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                temperature=0,
                messages=[
                    {
                        "role": "system",
                        "content":
                        """
    You are a Clinical Investigator AI.

    Requirements:

    - Ground every answer in supplied evidence.
    - Never hallucinate.
    - Never fabricate values.
    - Explain findings clearly.
    - Compare entities when requested.
    - Perform clinical reasoning when requested.
    - Identify important safety signals.
    - Identify abnormal laboratory findings.
    - Explain medication-diagnosis relationships.
    - Explain adverse event relationships.
    - Highlight uncertainty when evidence is insufficient.
    """
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
        )

        return (
            response
            .choices[0]
            .message
            .content
        )