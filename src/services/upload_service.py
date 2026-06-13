from src.ingestion.ingestion_service import IngestionService

from src.retrieval.index_builder import IndexBuilder

from src.retrieval.index_registry import (
    IndexRegistry
)


class UploadService:

    def __init__(self):

        self.ingestion = IngestionService()

        self.index_builder = IndexBuilder()

    def upload_file(self, file_path: str):

        # -------------------------
        # STEP 1: INGEST FILE
        # -------------------------
        result = self.ingestion.process_file(file_path)

        # -------------------------
        # STEP 2: REBUILD INDEX
        # -------------------------
        IndexRegistry.refresh()

        # -------------------------
        # STEP 3: RETURN RESULT
        # -------------------------
        return {
            "status": "success",
            "file": file_path,
            "result": result,
            "message": "Index refreshed successfully"
        }