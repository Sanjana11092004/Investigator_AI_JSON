from pathlib import Path

from src.ingestion.structured_converter import (
    StructuredConverter
)

from src.ingestion.pdf_converter import (
    PDFConverter
)


class IngestionService:

    def __init__(self):

        self.converter = (
            StructuredConverter()
        )

        self.pdf_converter = (
            PDFConverter()
        )

    def process_file(
        self,
        file_path: str
    ):

        path = Path(
            file_path
        )

        suffix = (
            path.suffix.lower()
        )

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

        if suffix == ".json":

            return (
                self.converter
                .process_study_json(
                    file_path
                )
            )

        if suffix == ".pdf":

            return (
                self.pdf_converter
                .process_pdf(
                    file_path
                )
            )

        raise ValueError(
            f"Unsupported file type: {suffix}"
        )