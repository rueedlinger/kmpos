from enum import Enum
from typing import Union
from pydantic import BaseModel
from datetime import datetime


class ArticleType(str, Enum):
    admin = "ADMIN"
    beverage = "BEVERAGE"
    food = "FOOD"


class Article(BaseModel):
    name: str
    articele_type: ArticleType
    price: float
    description: Union[str, None] = None


class Table(BaseModel):
    name: str
    is_active: bool = True


class Order(BaseModel):
    table: Table
    order_number: int
    items: list["OrderItem"] = []
    created_ts: datetime


class OrderItem(BaseModel):
    article: Article
    quantity: int = 1
