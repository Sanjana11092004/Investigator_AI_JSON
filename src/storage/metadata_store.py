import sqlite3
from datetime import datetime

from src.config.settings import settings


class MetadataStore:

    def __init__(self):

        self.db_path = settings.BASE_DIR / settings.DATABASE_PATH

        self._initialize()

    def _initialize(self):

        conn = sqlite3.connect(self.db_path)

        cursor = conn.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS documents (

                document_id TEXT PRIMARY KEY,

                category TEXT,

                source_file TEXT,

                source_type TEXT,

                json_path TEXT,

                created_at TEXT

            )
            """
        )

        conn.commit()
        conn.close()

    def register_document(
        self,
        document_id: str,
        category: str,
        source_file: str,
        source_type: str,
        json_path: str
    ):

        conn = sqlite3.connect(self.db_path)

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO documents
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                document_id,
                category,
                source_file,
                source_type,
                json_path,
                datetime.utcnow().isoformat()
            )
        )

        conn.commit()
        conn.close()