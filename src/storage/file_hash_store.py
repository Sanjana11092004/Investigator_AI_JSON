import hashlib
from pathlib import Path


class FileHashStore:

    @staticmethod
    def calculate_hash(
        file_path: str
    ) -> str:

        sha = hashlib.sha256()

        with open(file_path, "rb") as f:

            while chunk := f.read(8192):

                sha.update(chunk)

        return sha.hexdigest()