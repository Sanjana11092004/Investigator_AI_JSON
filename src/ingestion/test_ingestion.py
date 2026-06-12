from src.ingestion.ingestion_service import (
    IngestionService
)

service = IngestionService()

result = service.process_file(
    "incoming/sample.csv"
)

print(result)