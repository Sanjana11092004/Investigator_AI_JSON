from pathlib import Path

from src.ingestion.ingestion_service import (
    IngestionService
)

from src.retrieval.index_builder import (
    IndexBuilder
)


class UploadService:

    def __init__(self):

        self.ingestion = (
            IngestionService()
        )

    def upload_and_ingest(
        self,
        file_path: str
    ):

        result = (

            self.ingestion
            .process_file(
                file_path
            )

        )

        IndexBuilder().build()

        return {

            "status":
            "success",

            "file":
            Path(file_path).name,

            "result":
            result
        }