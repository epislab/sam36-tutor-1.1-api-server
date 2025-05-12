import os
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from fastapi.security import HTTPAuthorizationCredentials, OAuth2PasswordBearer
from jose import ExpiredSignatureError, JWTError, jwt
from fastapi import Depends, APIRouter, Body, HTTPException, Header, Request, Response, Security
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse
from typing import Annotated, Optional
from fastapi.responses import JSONResponse
from com.epislab.account.auth.user.api.user_controller import UserController
from com.epislab.account.auth.user.models.user_schema import UserLoginSchema, UserSchema
from com.epislab.utils.config.db_config import get_db
from com.epislab.utils.config.security.jwt_config import create_access_token
from com.epislab.utils.config.security.redis_config import redis_client

router = APIRouter()
controller = UserController()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = os.getenv("REFRESH_SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
security = HTTPBearer()

@router.get("/refresh")
async def refresh_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    incoming_token  = credentials.credentials 
    print("🎯 Authorization Header:", incoming_token )

    if not incoming_token :
        raise HTTPException(status_code=400, detail="💥💥💥💥 Refresh token is missing or malformed")
    
    # "Bearer " 제거 (혹시라도 남아 있을 경우)
    if incoming_token.startswith("Bearer "):
        incoming_token = incoming_token[len("Bearer "):].strip()

    try:
        # 2. JWT 디코드
        payload = jwt.decode(incoming_token , SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if not user_id:
            raise HTTPException(status_code=401, detail="💥💥💥💥 Invalid token payload")
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="💥💥💥💥 Refresh token has expired")
    except JWTError:
        raise HTTPException(status_code=401, detail="💥💥💥💥 Invalid refresh token")

    # 3. Redis에서 저장된 Refresh Token과 비교
    stored_token = await redis_client.get(f"refresh_token:{user_id}")
    print("🎯🎯🎯🎯 stored_token:", stored_token)

    if stored_token != incoming_token:
        raise HTTPException(status_code=401, detail="💥💥💥💥 Invalid refresh token")

    # 4. 사용자 정보 가져와서 반환
    logged_in_user: dict = dict({"user_id": "kim"})
    access_token = create_access_token(logged_in_user)
    return access_token


@router.post("/login", response_model=UserSchema)
async def handle_user(
    user_schema: UserLoginSchema = Body(...), 
    db: AsyncSession = Depends(get_db)):
    content = await controller.login(user_schema=user_schema, db=db)
    return JSONResponse(content=content)


