from src.llm.groq_service import (
    GroqService
)

from src.llm.prompts import (
    CLINICAL_EXTRACTION_PROMPT
)

sample = """
PAT-1

41 year old male

Diagnoses:
Rheumatoid Arthritis
Osteoporosis

Medications:
Warfarin
Carvedilol
"""

service = GroqService()

result = service.extract_clinical_json(
    sample,
    CLINICAL_EXTRACTION_PROMPT
)

print(result)