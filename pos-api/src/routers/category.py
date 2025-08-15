from fastapi import APIRouter

from rest.category import CategoryRead


router = APIRouter(prefix="/category", tags=["category"])

@router.get(
    "/",
    summary="Get categories",
    response_model=list[CategoryRead],
)
def get_articles():
    return None


@router.get(
    "/{category_id}",
    summary="Get category by ID",
    response_model=CategoryRead,
)
def get_article_by_id(category_id: int):
    return None