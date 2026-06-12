from fastapi import APIRouter

from src.services.session_service import (
    SessionService
)

router = APIRouter()

service = SessionService()


@router.get(
    "/{session_id}"
)
def get_session(
    session_id: str
):

    return (
        service.get_session(
            session_id
        )
    )   