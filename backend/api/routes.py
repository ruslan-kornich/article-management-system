from fastapi import APIRouter
from backend.api.endpoints import (
    signup,
    login,
    get_articles,
    create_article,
    update_article,
    delete_article,
)

router = APIRouter()

router.include_router(signup.router, tags=["signup"])
router.include_router(login.router, tags=["login"])
router.include_router(get_articles.router, tags=["articles"])
router.include_router(create_article.router, tags=["articles"])
router.include_router(update_article.router, tags=["articles"])
router.include_router(delete_article.router, tags=["articles"])
