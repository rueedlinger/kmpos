from rest.internal import AppInfo

from fastapi import APIRouter

from core import get_version
from persistence import get_session_deps


router = APIRouter(prefix="/app", tags=["app"])


get_session_deps()


@router.get(
    "/info",
    summary="Application information's",
    response_model=AppInfo,
)
def get_health() -> AppInfo:
    return AppInfo.model_validate(
        {"version": get_version(), "details": {"name": "kmpos"}}
    )
