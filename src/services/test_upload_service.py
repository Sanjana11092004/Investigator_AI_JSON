from src.services.upload_service import (
    UploadService
)

service = (
    UploadService()
)

result = (

    service.upload_and_ingest(
        "incoming/SDTM_100patients.xlsx"
    )

)

print(result)