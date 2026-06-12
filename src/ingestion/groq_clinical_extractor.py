from src.llm.groq_service import (
    GroqService
)

from src.llm.prompts import (
    CLINICAL_EXTRACTION_PROMPT
)


class GroqClinicalExtractor:

    def __init__(self):

        self.groq = GroqService()

    def extract_patient(
        self,
        text: str
    ) -> dict:

        return (
            self.groq
            .extract_clinical_json(
                text,
                CLINICAL_EXTRACTION_PROMPT
            )
        )