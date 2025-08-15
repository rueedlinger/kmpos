import datetime
from enum import Enum
from pydantic import BaseModel

from rest.article import ArticleType


class OrderStatus(str, Enum):
    PENDING = "PENDING"
    STORNO = "STORNO"
    PAID = "PAID"

class PrintStatus(str, Enum):
    PENDING = "PENDING"
    COMPLETE = "COMPLETE"
    PARTIAL = "PARTIAL"


class OrderItemRead(BaseModel):
    id: int
    article_id: int
    article_name: str
    artcile_type: ArticleType
    print_status: PrintStatus = PrintStatus.PENDING
    comment: str | None = None
    quantity: int
    price: float
    total: float

class OrderRead(BaseModel):
    id: int
    user_id: int
    user_ip: str | None = None
    table_id: int 
    table_name: str
    print_status: PrintStatus = PrintStatus.PENDING
    status: OrderStatus = OrderStatus.PENDING
    total: float
    items: list[OrderItemRead] 
    order_ts: datetime.datetime
   
 
    
    
   