from pydantic import BaseModel

from model.pos import Article


class CartItrem(BaseModel):
    article: Article
    quantity: int


class Cart(BaseModel):
    id: str
    items: list[CartItrem] = []
    ip: str | None = None
