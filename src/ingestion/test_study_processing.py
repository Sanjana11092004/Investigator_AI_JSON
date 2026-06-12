# src/ingestion/test_study_processing.py
from src.ingestion.structured_converter import StructuredConverter

converter = StructuredConverter()

result = converter.process_study_json(
    "incoming/Study 1.json"
)

print(result)