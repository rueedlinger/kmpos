from typing import Optional
from pydantic import BaseModel
from enum import Enum

from rest.order import OrderRead

    
class TableRead(BaseModel):
    id: int 
    name: str
    description: str | None = None   
    is_active: bool = True   
    order: int = 0

class TableReadHistory(BaseModel):
    id: int 
    name: str
    description: str | None = None   
    is_active: bool = True   
    order: int = 0
    history: Optional[list[OrderRead]] = None