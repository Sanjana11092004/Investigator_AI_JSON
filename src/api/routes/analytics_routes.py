from fastapi import APIRouter

from src.services.analytics_service import (
    AnalyticsService
)

router = APIRouter()

service = AnalyticsService()


@router.get(
    "/summary"
)
def analytics_summary():

    return (
        service.summary()
    )