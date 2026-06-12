from pathlib import Path

from src.ingestion.structured_converter import (
    StructuredConverter
)

converter = StructuredConverter()

study_files = Path(
    "incoming"
).glob("Study *.json")

for study_file in study_files:

    result = converter.process_study_json(
        str(study_file)
    )

    print(result)