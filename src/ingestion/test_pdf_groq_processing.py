from pathlib import Path

from src.ingestion.pdf_processor import (
    PDFProcessor
)

from src.ingestion.groq_clinical_extractor import (
    GroqClinicalExtractor
)

from src.models.document_models import (
    ClinicalDocument
)

from src.storage.json_store import (
    JSONStore
)


pdf_file = next(
    Path("incoming").glob("*.pdf")
)

processor = PDFProcessor()

text = processor.extract_text(
    str(pdf_file)
)

# Temporary split
# We will improve later

chunks = text.split(
    "CLINICAL NARRATIVE NOTE"
)

extractor = (
    GroqClinicalExtractor()
)

patients = []

for chunk in chunks:

    chunk = chunk.strip()

    if len(chunk) < 100:
        continue

    try:

        patient = (
            extractor
            .extract_patient(
                chunk
            )
        )

        patients.append(
            patient
        )

        print(
            f"Processed patient: "
            f"{patient.get('patient_id')}"
        )

    except Exception as e:

        print(
            f"Error: {e}"
        )

document = ClinicalDocument(
    file_name="clinical_narratives",
    source_file=pdf_file.name,
    source_type="pdf",
    category="patients",
    metadata={
        "patient_count": len(
            patients
        )
    },
    data={
        "patients": patients
    }
)

store = JSONStore()

output = store.save_document(
    document
)

print(
    f"\nSaved: {output}"
)

print(
    f"Patients: {len(patients)}"
)