from fastapi import APIRouter

from src.services.query_service import (
    QueryService
)

router = APIRouter()

service = QueryService()


@router.get(
    "/subject/{subject_id}"
)
def get_subject(
    subject_id: str
):

    return service.get_subject(
        subject_id
    )


@router.get(
    "/study/{study_id}"
)
def get_study(
    study_id: str
):

    return service.get_study(
        study_id
    )


@router.get(
    "/patient/{patient_id}"
)
def get_patient(
    patient_id: str
):

    return service.get_patient(
        patient_id
    )