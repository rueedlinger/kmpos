from fastapi import APIRouter
from rest.order import OrderRead

router = APIRouter(prefix="/order", tags=["order"])

@router.get(
    "/",
    summary="Get orders",
    response_model=list[OrderRead],
)
def get_orders():
    return None


@router.get(
    "/{order_id}",
    summary="Get a order by ID",
    response_model=OrderRead,
)
def get_order(
    order_id: int,
) -> OrderRead:
    return None

