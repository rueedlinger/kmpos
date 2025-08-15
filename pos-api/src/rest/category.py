from pydantic import BaseModel


class CategoryRead(BaseModel):
    id: int
    name: str
    description: str | None = None    
    is_active: bool = True
    order: int = 0
