from src.ingestion.ingestion_service import (
    IngestionService
)

service = (
    IngestionService()
)

result = (
    service.process_file(
        "uploads/Medical_Narratives.pdf"
    )
)

print(result)