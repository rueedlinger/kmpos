import datetime
import uuid
from pydantic import BaseModel

from rest.article import ArticleRead
from rest.order import OrderItemRead

class BasketItemRead(BaseModel):
    article: ArticleRead
    comment: str | None = None
    quantity: int
    total: float


class BasketRead(BaseModel):
    id: str = str(uuid.uuid4())
    user_id: int
    user_ip: str | None = None
    table_id: int 
    items: list[BasketItemRead]
    total: float
    basket_ts: datetime.datetime