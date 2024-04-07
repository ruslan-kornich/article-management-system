from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List
from backend.database.database import get_db
from backend.core.models.article import Article
from backend.schemas import ArticleSchema

router = APIRouter()


@router.get("/articles/", response_model=List[ArticleSchema])
def get_articles(
        skip: int = Query(0, description="Number of items to skip"),
        limit: int = Query(10, description="Number of items to retrieve"),
        search: str = Query(None, description="Search term to filter articles"),
        db: Session = Depends(get_db)
):
    query = db.query(Article).order_by(Article.published.desc())

    # Filtering by search query, if any
    if search:
        query = query.filter(Article.title.ilike(f"%{search}%"))

    # Pagination
    articles = query.offset(skip).limit(limit).all()

    return [
        {
            "id": article.id,
            "title": article.title,
            "link": article.link,
            "summary": article.summary,
            "published": article.published.strftime("%Y-%m-%d %H:%M:%S"),
            "author": article.author,
        }
        for article in articles
    ]
