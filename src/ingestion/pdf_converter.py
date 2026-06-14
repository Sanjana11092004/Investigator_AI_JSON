from pathlib import Path

from src.ingestion.pdf_processor import (
    PDFProcessor
)

from src.ingestion.smart_segmenter import (
    SmartSegmenter
)

from src.ingestion.groq_clinical_extractor import (
    GroqClinicalExtractor
)

from src.models.document_models import (
    ClinicalDocument
)

from src.storage.file_hash_store import (
    FileHashStore
)

from src.storage.json_store import (
    JSONStore
)

from src.storage.metadata_store import (
    MetadataStore
)


class PDFConverter:

    def __init__(self):

        self.pdf_processor = (
            PDFProcessor()
        )

        self.splitter = (
            SmartSegmenter()
        )

        self.extractor = (
            GroqClinicalExtractor()
        )

        self.json_store = (
            JSONStore()
        )

        self.metadata_store = (
            MetadataStore()
        )

    def process_pdf(
        self,
        file_path: str
    ):

        file_hash = (
            FileHashStore.calculate_hash(
                file_path
            )
        )

        if self.metadata_store.file_exists(
            file_hash
        ):

            print(
                "File already processed. Skipping."
            )

            return None

        text = (
            self.pdf_processor
            .extract_text(
                file_path
            )
        )

        narratives = (
            self.splitter
            .split(text)
        )

        patients = []

        total = len(
            narratives
        )

        for index, narrative in enumerate(
            narratives,
            start=1
        ):

            print(
                f"Processing patient "
                f"{index}/{total}"
            )

            patient = (
                self.extractor
                .extract_patient(
                    narrative
                )
            )

            patients.append(
                patient
            )

        document = ClinicalDocument(

            file_name=Path(
                file_path
            ).stem,

            source_file=Path(
                file_path
            ).name,

            source_type="pdf",

            category="patients",

            metadata={
                "patient_count":
                len(patients)
            },

            data={
                "patients":
                patients
            }
        )

        output_path = (
            self.json_store
            .save_document(
                document
            )
        )

        self.metadata_store.register_document(

            document_id=
            document.document_id,

            category=
            document.category,

            source_file=
            document.source_file,

            source_type=
            document.source_type,

            json_path=
            str(output_path),

            file_hash=
            file_hash
        )

        return {
            "patient_count":
            len(patients),

            "output":
            str(output_path)
        }