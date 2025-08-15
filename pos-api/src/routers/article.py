from fastapi import APIRouter

from rest.article import ArticleRead



router = APIRouter(prefix="/article", tags=["article"])

@router.get(
    "/",
    summary="Get articles",
    response_model=list[ArticleRead],
)
def get_articles():
    return None


@router.get(
    "/{article_id}",
    summary="Get article by ID",
    response_model=ArticleRead,
)
def get_article_by_id(article_id: int):
    return None