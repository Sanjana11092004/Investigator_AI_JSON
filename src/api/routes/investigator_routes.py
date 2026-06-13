from fastapi import APIRouter

from src.services.investigator_assessment_service import (
    InvestigatorAssessmentService
)

from src.services.investigator_service import (
    InvestigatorService
)

from src.api.schemas.request_models import (
    ChatRequest
)

from src.api.schemas.response_models import (
    ChatResponse
)

router = APIRouter()

assessment_service = (
    InvestigatorAssessmentService()
)

investigator_service = (
    InvestigatorService()
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

        assessment_service
        .generate_subject_assessment(
            subject_id
        )

    )


@router.post(
    "/chat",
    response_model=ChatResponse
)
def investigator_chat(
    request: ChatRequest
):

    response = (

        investigator_service
        .ask(

            question=
            request.question,

            session_id=
            request.session_id

        )

    )

    return {

        "response":
        response

    }