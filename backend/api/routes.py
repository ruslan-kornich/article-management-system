from fastapi import APIRouter
from backend.api.endpoints import signup, login, get_articles

router = APIRouter()

router.include_router(signup.router, tags=["user"])
router.include_router(login.router, tags=["user"])
router.include_router(get_articles.router, tags=["post"])

