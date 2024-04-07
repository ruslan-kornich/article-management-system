from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from backend.database.database import get_db
from backend.core.models.article import Article
from backend.schemas import ArticleSchema

router = APIRouter()


@router.get("/articles/", response_model=List[ArticleSchema])
def get_articles(db: Session = Depends(get_db)):
    articles = db.query(Article).all()
    return [{"id": article.id,
             "title": article.title,
             "link": article.link,
             "summary": article.summary,
             "published": article.published.strftime('%Y-%m-%d %H:%M:%S'),
             "author": article.author} for article in articles]
