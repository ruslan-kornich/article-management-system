from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database.database import get_db
from backend.core.models.article import Article as ModelArticle
from backend.schemas import ArticleSchema
from backend.security import get_current_user
from backend.core.models.user import User as ModelUser

router = APIRouter()


@router.delete("/articles/{article_id}", response_model=dict)
async def delete_article(
    article_id: int,
    db: Session = Depends(get_db),
    current_user: ModelUser = Depends(get_current_user),
):
    db_article = db.query(ModelArticle).filter(ModelArticle.id == article_id).first()
    if not db_article:
        raise HTTPException(status_code=404, detail="Article not found")
    db.delete(db_article)
    db.commit()
    return {"detail": "Article deleted successfully"}
