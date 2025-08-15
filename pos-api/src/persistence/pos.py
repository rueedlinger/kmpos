from datetime import datetime
from enum import Enum
from sqlmodel import Field, Relationship, SQLModel


class ArticleType(str, Enum):
    ADMIN = "ADMIN"
    BEVERAGE = "BEVERAGE"
    FOOD = "FOOD"


class ArticleCategory(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str | None = None
    is_active: bool = True
    order: int = 0
    articles: list["Article"] = Relationship(back_populates="category")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)    


class Article(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    category_id: int | None = Field(default=None, foreign_key="article.id")
    name: str
    description: str | None = None
    price: float
    is_coupon: bool = False
    article_type: ArticleType | None = Field(index=True)
    is_active: bool = True
    order: int = 0
    category: ArticleCategory | None = Relationship(back_populates="articles")
    order_items: list["OrderItem"] = Relationship(back_populates="article")
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

class Table(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str | None = None
    is_active: bool = True
    order: int = 0
    orders: list["Order"] = Relationship(back_populates="table")
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str
    password: str
    is_active: bool = True
    is_admin: bool = False
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

class Transaction(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    order_id: int | None = Field(default=None, foreign_key="order.id")
    ip: str | None = None
    order: list["Order"] | None = Relationship(back_populates="transactions")
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

class Order(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    table_id: int | None = Field(default=None, foreign_key="table.id")
    total_amount: float = 0.0
    table: Table | None = Relationship(back_populates="orders")
    items: list["OrderItem"] = Relationship(back_populates="order")
    transactions: list[Transaction] = Relationship(back_populates="order")
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

class OrderItem(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    article_id: int | None = Field(default=None, foreign_key="article.id")
    order_id: int | None = Field(default=None, foreign_key="order.id")
    quantity: int = 1
    price: float = 0.0
    comment: str | None = None
    article: Article | None = Relationship(back_populates="order_items")
    order: Order | None = Relationship(back_populates="items")
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)