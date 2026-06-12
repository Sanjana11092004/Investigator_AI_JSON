from fastapi import APIRouter

from src.services.investigator_assessment_service import (
    InvestigatorAssessmentService
)

router = APIRouter()

service = (
    InvestigatorAssessmentService()
)


@router.post(
    "/subject-assessment"
)
def subject_assessment(
    payload: dict
):

    subject_id = (
        payload.get(
            "subject_id"
        )
    )

    return (

        service.generate_subject_assessment(
            subject_id
        )

    )