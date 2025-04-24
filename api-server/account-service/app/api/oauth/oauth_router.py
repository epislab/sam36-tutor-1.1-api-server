from fastapi import APIRouter, Depends
from app.domain.oauth.controllers.oauth_controller import OAuthController

router = APIRouter(prefix="/oauth", tags=["oauth"])

@router.post("/token")
async def get_token():
    return {"message": "OAuth token endpoint"} 