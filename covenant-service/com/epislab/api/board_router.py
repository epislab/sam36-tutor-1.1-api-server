from fastapi import APIRouter
from com.epislab.api.board.article_router import router as article_router

router = APIRouter()

router.include_router(article_router, prefix="/article")
