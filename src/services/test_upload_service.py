from src.services.upload_service import (
    UploadService
)

service = (
    UploadService()
)

result = (

    service.upload_file(
        "uploads/SDTM_100patients.xlsx"
    )

)

print(result)