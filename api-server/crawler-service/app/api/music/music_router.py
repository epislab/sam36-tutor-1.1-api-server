from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, APIRouter, Body, Response
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse
from typing import Annotated
from fastapi.responses import JSONResponse

from app.domain.music.music_controller import MusicController

import logging

logging.basicConfig(level=logging.INFO)



router = APIRouter()
controller = MusicController()



@router.get("/music")
async def handle_music():
    logging.info("🔑🔑🔑🔑🔑🔑멜론 차트 크롤링 시작")

    result = await controller.get_melon_chart()
    return "크롤러 테스트"

