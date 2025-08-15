from typing import Annotated
from fastapi import APIRouter, Request

from core.http import PosException
from rest.table import TableRead, TableReadHistory



router = APIRouter(prefix="/table", tags=["table"])


@router.get(
    "/",
    summary="Get tables",
    response_model=list[TableRead],
)
def getget_tables() -> list[TableRead]:
    return None

@router.get(
    "/{table_id}",
    summary="Get a table by ID",
    response_model=TableReadHistory,
)
def get_table(table_id: str) -> TableReadHistory:
    pass

