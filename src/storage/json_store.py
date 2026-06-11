from pathlib import Path

import orjson

from src.config.settings import settings
from src.models.document_models import ClinicalDocument


class JSONStore:

    def save_document(
        self,
        document: ClinicalDocument
    ) -> Path:

        category_dir = (
            settings.JSON_STORE_DIR
            / document.category
        )

        category_dir.mkdir(
            parents=True,
            exist_ok=True
        )

        file_path = (
            category_dir
            / f"{document.document_id}.json"
        )

        with open(file_path, "wb") as f:

            f.write(
                orjson.dumps(
                    document.model_dump(mode="json"),
                    option=orjson.OPT_INDENT_2
                )
            )

        return file_path

    def load_document(
        self,
        path: Path
    ) -> dict:

        with open(path, "rb") as f:

            return orjson.loads(
                f.read()
            )