from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database.database import get_db
from backend.core.models.article import Article as ModelArticle
from backend.schemas import ArticleSchema, ArticleUpdate
from backend.security import get_current_user
from backend.core.models.user import User as ModelUser

router = APIRouter()


@router.put("/articles/{article_id}", response_model=ArticleSchema)
async def update_article(
    article_id: int,
    article: ArticleUpdate,
    db: Session = Depends(get_db),
    current_user: ModelUser = Depends(get_current_user),
):
    db_article = db.query(ModelArticle).filter(ModelArticle.id == article_id).first()
    if not db_article:
        raise HTTPException(status_code=404, detail="Article not found")

    update_data = article.dict(exclude_unset=True)

    # Convert Url object to string
    if "link" in update_data:
        update_data["link"] = str(update_data["link"])

    for key, value in update_data.items():
        setattr(db_article, key, value)

    db.commit()
    db.refresh(db_article)
    return db_article
