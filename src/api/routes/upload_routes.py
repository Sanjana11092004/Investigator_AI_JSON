from fastapi import APIRouter

router = APIRouter()


@router.get(
    "/health"
)
def upload_health():

    return {
        "status": "upload route ready"
    } 