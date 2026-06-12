from pathlib import Path

from loguru import logger

from src.ingestion.file_normalizer import (
    FileNormalizer
)


class IngestionService:

    def process_file(
        self,
        file_path: str
    ):

        path = Path(file_path)

        file_type = (
            FileNormalizer.get_file_type(path)
        )

        logger.info(
            f"Processing {path.name}"
        )

        logger.info(
            f"Detected type: {file_type}"
        )

        return {
            "file_name": path.name,
            "file_type": file_type
        }