"""
OAuth 라우터
- OAuth 인증/인가 엔드포인트
- 토큰 관리
- 사용자 인증 처리
"""

from fastapi import APIRouter, Depends, HTTPException
from typing import Dict, Any

router = APIRouter(
    prefix="/oauth",
    tags=["oauth"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def root() -> Dict[str, Any]:
    """
    OAuth 서비스 루트 엔드포인트
    """
    return {"message": "OAuth Service"} 