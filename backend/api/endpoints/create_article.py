from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database.database import get_db
from backend.core.models.article import Article as ModelArticle
from backend.schemas import ArticleSchema, ArticleCreate
from backend.security import get_current_user
from backend.core.models.user import User as ModelUser
from urllib.parse import urlparse

router = APIRouter()


@router.post("/articles/", response_model=ArticleSchema)
async def create_article(
    article: ArticleCreate,
    db: Session = Depends(get_db),
    current_user: ModelUser = Depends(get_current_user),
):
    author_email = article.author if article.author else current_user.email

    # Преобразование объекта Url в строку
    link_str = str(article.link)

    db_article = ModelArticle(
        title=article.title,
        link=link_str,
        summary=article.summary,
        published=article.published,
        author=author_email,
    )

    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article
