

from typing import Annotated
import uuid
from cachetools import TTLCache
from fastapi import APIRouter, HTTPException, Request
from fastapi.params import Header

from core.http import PosException
from model.cart import Cart


router = APIRouter(prefix="/cart", tags=["cart"])

cache = TTLCache(maxsize=1024, ttl=600)



@router.get(
   "/{cart_id}",
    summary="Get a cart by ID",
    response_model=Cart,
)
def get_cart(cart_id: str,) -> Cart:
     
     if cart_id in cache:
         return cache[cart_id]
     raise PosException(name="Cart Not Found", message=f"Cart with id '{cart_id}' not found", code=404)
     

@router.put(
    "/{cart_id}",
    summary="Update an existing cart",
    response_model=Cart,
)
def update_cart(cart_id: str, cart: Cart, request: Request) -> Cart:
    # Here you would typically update the cart in a database
    cart.id = cart_id
    cart.ip  = request.client.host   
    cache[cart_id] = cart
    return cart


@router.get(
    "/",
    summary="List all carts",
    response_model=list[Cart],
)
def list_carts() -> list[Cart]:
    return list(cache.values())