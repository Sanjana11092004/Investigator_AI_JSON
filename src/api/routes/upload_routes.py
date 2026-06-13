from pathlib import Path
import shutil

from fastapi import (
    APIRouter,
    UploadFile,
    File
)

from src.services.upload_service import (
    UploadService
)

router = APIRouter()

UPLOAD_DIR = Path(
    "uploads"
)

UPLOAD_DIR.mkdir(
    exist_ok=True
)

service = UploadService()


@router.post(
    "/upload"
)
async def upload_file(

    file: UploadFile = File(...)

):

    destination = (

        UPLOAD_DIR
        / file.filename

    )

    with open(
        destination,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    result = (

        service.upload_and_ingest(
            str(destination)
        )

    )

    return result


@router.get(
    "/health"
)
def upload_health():

    return {
        "status":
        "upload route ready"
    }