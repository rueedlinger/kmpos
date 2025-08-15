from pydantic import BaseModel
from enum import Enum


class ArticleType(str, Enum):
    ADMIN = "ADMIN"
    BEVERAGE = "BEVERAGE"
    FOOD = "FOOD"

    
class ArticleRead(BaseModel):
    id: int 
    name: str
    description: str | None = None
    price: float
    is_coupon: bool = False
    is_active: bool = True
    category_id: int
    category_name: str
    type: ArticleType = ArticleType.ADMIN
    order: int = 0