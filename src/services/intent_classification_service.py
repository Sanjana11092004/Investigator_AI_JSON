import json
import re

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

IMPORTANT:

Use the active entity, previous questions,
previous answers, and conversation history
to resolve follow-up questions.

Examples:

Previous:
Summarize patient PT-101

Current:
What medications is she taking?

Return:

{{
    "intent": "patient",
    "entity_type": "patient",
    "entity_id": "PT-101",
    "action": "medications",
    "metric": null
}}

Previous:
Summarize study NCT01007279

Current:
Who sponsored it?

Return:

{{
    "intent": "study",
    "entity_type": "study",
    "entity_id": "NCT01007279",
    "action": "retrieve",
    "metric": null
}}

Previous:
Summarize subject SUBJ-0001

Current:
Any lab abnormalities?

Return:

{{
    "intent": "subject",
    "entity_type": "subject",
    "entity_id": "SUBJ-0001",
    "action": "labs",
    "metric": null
}}

Question:
How many participants?

Return:

{{
    "intent": "analytics",
    "entity_type": "cohort",
    "entity_id": null,
    "action": "count",
    "metric": "participants"
}}

Question:
How many females?

Return:

{{
    "intent": "analytics",
    "entity_type": "cohort",
    "entity_id": null,
    "action": "count",
    "metric": "female"
}}

Question:
How many males?

Return:

{{
    "intent": "analytics",
    "entity_type": "cohort",
    "entity_id": null,
    "action": "count",
    "metric": "male"
}}

Question:
Average age?

Return:

{{
    "intent": "analytics",
    "entity_type": "cohort",
    "entity_id": null,
    "action": "average",
    "metric": "age"
}}

Question:
Maximum ALT value?

Return:

{{
    "intent": "analytics",
    "entity_type": "cohort",
    "entity_id": null,
    "action": "max",
    "metric": "alanine aminotransferase"
}}

Question:
Minimum Creatinine?

Return:

{{
    "intent": "analytics",
    "entity_type": "cohort",
    "entity_id": null,
    "action": "min",
    "metric": "creatinine"
}}

Question:
Most common adverse event?

Return:

{{
    "intent": "analytics",
    "entity_type": "cohort",
    "entity_id": null,
    "action": "frequency",
    "metric": "adverse_event"
}}

Question:
Summarize patient PT-101

Return:

{{
    "intent": "patient",
    "entity_type": "patient",
    "entity_id": "PT-101",
    "action": "summarize",
    "metric": null
}}

Question:
Summarize subject SUBJ-0001

Return:

{{
    "intent": "subject",
    "entity_type": "subject",
    "entity_id": "SUBJ-0001",
    "action": "summarize",
    "metric": null
}}

Question:
Summarize study NCT01007279

Return:

{{
    "intent": "study",
    "entity_type": "study",
    "entity_id": "NCT01007279",
    "action": "summarize",
    "metric": null
}}

Question:
How many participants were enrolled in NCT01007279?

Return:

{{
    "intent": "study",
    "entity_type": "study",
    "entity_id": "NCT01007279",
    "action": "retrieve",
    "metric": "enrollment"
}}

Determine:

1. intent
2. entity_type
3. entity_id
4. action
5. metric

Allowed intents:

study
subject
patient
cohort
analytics
out_of_scope

Allowed actions:

IMPORTANT:

The words:
- summarize
- summary
- overview

must map to:

action = summarize

summarize
retrieve
demographics
medications
labs
adverse_events
diagnosis
compare
explain

count
average
min
max
frequency

unknown

IMPORTANT:

Questions about:
- sponsor
- enrollment
- participants enrolled
- outcomes
- eligibility
- location
- phase
- status
- intervention

must be classified as:

intent = study
action = retrieve

NOT analytics


IMPORTANT:

- Use session context when entity is omitted.
- Resolve references such as:
  - he
  - she
  - this patient
  - this subject
  - this study
  - it

IMPORTANT:

Only use session memory for true follow-up questions.

Examples:

Previous:
Summarize PT-101

Current:
What medications is she taking?

Use PT-101.

Previous:
Summarize NCT01007279

Current:
Who sponsored it?

Use NCT01007279.

DO NOT use session memory for discovery questions.

Examples:

Who was a professional athlete?
Which patient had atrial fibrillation?
Who had ankle swelling?
Which patient worked as a school principal?

For such questions return:

{{
    "intent": "patient",
    "entity_type": "patient",
    "entity_id": null,
    "action": "retrieve",
    "metric": null
}}

CRITICAL:

Return ONLY a JSON object.

Do not explain.
Do not add reasoning.
Do not add markdown.
Do not add code fences.
Do not add any text before or after the JSON.

Question:
{question}

Output Format:

{{
    "intent": "...",
    "entity_type": "...",
    "entity_id": "...",
    "action": "...",
    "metric": "..."
}}
"""

        response = (
            self.groq.generate(
                prompt
            )
        )

        print("\nRAW CLASSIFIER RESPONSE:")
        print(response)
        print()

        if response.startswith("```"):

            response = (
                response
                .replace("```json", "")
                .replace("```", "")
                .strip()
            )

        try:

            start = response.find("{")

            end = response.rfind("}")

            if (
                start != -1
                and
                end != -1
            ):

                return json.loads(
                    response[
                        start:end+1
                    ]
                )

        except Exception as e:

            print(
                "CLASSIFIER PARSE ERROR:",
                e
            )

        return {
            "intent": "out_of_scope",
            "entity_type": "none",
            "entity_id": None,
            "action": "unknown",
            "metric": None
        }


if __name__ == "__main__":

    service = (
        IntentClassificationService()
    )

    print(
        service.classify(
            "Average age?",
            {}
        )
    )