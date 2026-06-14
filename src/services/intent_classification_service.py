import json

from src.llm.groq_service import (
    GroqService
)


class IntentClassificationService:

    def __init__(self):

        self.groq = (
            GroqService()
        )

    def classify(
        self,
        question: str,
        session_context: dict
    ):

        prompt = f"""
You are the intent engine for a Clinical Investigator AI.

Current Session Context:

{json.dumps(session_context, indent=2)}

Determine:

1. intent
2. entity_type
3. entity_id
4. action

Allowed intents:
study
subject
patient
cohort
analytics
out_of_scope

Allowed actions:
summarize
retrieve
demographics
medications
labs
adverse_events
diagnosis
analytics
compare
explain
unknown

IMPORTANT:

- Use session context when entity is omitted.
- Resolve references such as:
  - he
  - she
  - this patient
  - this subject
  - this study
  - it
- Return ONLY valid JSON.

Question:
{question}

Output Format:

{{
    "intent": "...",
    "entity_type": "...",
    "entity_id": "...",
    "action": "..."
}}
"""

        response = (
            self.groq.generate(
                prompt
            )
        )

        if response.startswith("```"):

            response = (
                response
                .replace("```json", "")
                .replace("```", "")
                .strip()
            )

        try:

            return json.loads(
                response
            )

        except Exception:

            return {
                "intent": "out_of_scope",
                "entity_type": "none",
                "entity_id": None,
                "action": "unknown"
            }