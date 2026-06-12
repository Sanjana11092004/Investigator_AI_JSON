from pathlib import Path


class FileNormalizer:

    STRUCTURED_EXTENSIONS = {
        ".csv",
        ".xls",
        ".xlsx",
        ".json"
    }

    UNSTRUCTURED_EXTENSIONS = {
        ".pdf",
        ".doc",
        ".docx"
    }

    @classmethod
    def get_file_type(
        cls,
        file_path: Path
    ) -> str:

        suffix = file_path.suffix.lower()

        if suffix in cls.STRUCTURED_EXTENSIONS:
            return "structured"

        if suffix in cls.UNSTRUCTURED_EXTENSIONS:
            return "unstructured"

        raise ValueError(
            f"Unsupported file type: {suffix}"
        )