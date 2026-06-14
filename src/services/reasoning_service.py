from src.llm.groq_service import (
    GroqService
)

from src.services.context_builder import (
    ContextBuilder
)


class ReasoningService:

    def __init__(self):

        self.groq = (
            GroqService()
        )

        self.context_builder = (
            ContextBuilder()
        )

    def reason(
        self,
        question: str,
        context: str
    ):

        prompt = f"""
You are a senior Clinical Investigator.

Your role is to reason over the supplied clinical evidence.

Rules:

- Use ONLY the supplied context.
- Never invent facts.
- Never assume unavailable data.
- Identify clinically relevant findings.
- Explain relationships between:
  diagnoses,
  medications,
  laboratory findings,
  adverse events,
  demographics,
  study characteristics.
- Highlight potential risks.
- Highlight abnormalities.
- Highlight investigator concerns.
- Explain possible clinical significance.
- Explain possible causality when supported.
- If evidence is insufficient, explicitly state that.

Question:

{question}

Clinical Context:

{context}

Answer:
"""

        return (
            self.groq.generate(
                prompt
            )
        )

    def compare_patients(
        self,
        question: str,
        patient_1: dict,
        patient_2: dict
    ):

        context = f"""

PATIENT A

{self.context_builder.build_patient_context(patient_1)}

PATIENT B

{self.context_builder.build_patient_context(patient_2)}

"""

        return (
            self.reason(
                question,
                context
            )
        )

    def compare_subjects(
        self,
        question: str,
        subject_1: dict,
        subject_2: dict
    ):

        context = f"""

SUBJECT A

{self.context_builder.build_subject_context(subject_1)}

SUBJECT B

{self.context_builder.build_subject_context(subject_2)}

"""

        return (
            self.reason(
                question,
                context
            )
        )

    def compare_studies(
        self,
        question: str,
        study_1: dict,
        study_2: dict
    ):

        context = f"""

STUDY A

{self.context_builder.build_study_context(study_1)}

STUDY B

{self.context_builder.build_study_context(study_2)}

"""

        return (
            self.reason(
                question,
                context
            )
        )

    def reason_over_entity(
        self,
        question: str,
        context: str
    ):

        return (
            self.reason(
                question,
                context
            )
        )