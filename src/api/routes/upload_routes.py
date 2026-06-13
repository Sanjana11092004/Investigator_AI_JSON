from fastapi import APIRouter, UploadFile, File

import shutil

from src.services.upload_service import UploadService

router = APIRouter()

service = UploadService()


@router.post("/upload")
def upload_file(file: UploadFile = File(...)):

    upload_path = f"uploads/{file.filename}"

    with open(upload_path, "wb") as buffer:

        shutil.copyfileobj(file.file, buffer)

    result = service.upload_file(upload_path)

    return result


@router.get("/health")
def upload_health():

    return {
        "status": "upload route ready"
    }