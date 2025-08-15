from fastapi import APIRouter
from rest.basket import BasketRead


router = APIRouter(prefix="/basket", tags=["basket"])

@router.get(
    "/",
    summary="Get bakstets",
    response_model=list[BasketRead],
)
def get_orders():
    return None


@router.get(
    "/{basket_id}",
    summary="Get a basket by ID",
    response_model=BasketRead,
)
def get_order(
    order_id: int,
) -> BasketRead:
    return None

