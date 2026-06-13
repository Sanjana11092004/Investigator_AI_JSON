from pathlib import Path

from src.ingestion.structured_converter import (
    StructuredConverter
)

from src.ingestion.pdf_processor import (
    PDFProcessor
)


class IngestionService:

    def __init__(self):

        self.converter = (
            StructuredConverter()
        )

        self.pdf_processor = (
            PDFProcessor()
        )

    def process_file(
        self,
        file_path: str
    ):

        path = Path(file_path)

        suffix = (
            path.suffix.lower()
        )

        # -------------------------
        # EXCEL
        # -------------------------

        if suffix in [

            ".xlsx",
            ".xls"

        ]:

            return (

                self.converter
                .process_excel(
                    file_path
                )

            )

        # -------------------------
        # STUDY JSON
        # -------------------------

        if suffix == ".json":

            return (

                self.converter
                .process_study_json(
                    file_path
                )

            )

        # -------------------------
        # PDF
        # -------------------------

        if suffix == ".pdf":

            text = (

                self.pdf_processor
                .extract_text(
                    file_path
                )

            )

            return {

                "file_type": "pdf",
                "characters": len(text),
                "preview": text[:500]

            }

        raise ValueError(
            f"Unsupported file type: {suffix}"
        )