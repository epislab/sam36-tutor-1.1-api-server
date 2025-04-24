from pydantic import BaseModel
from typing import Optional

class Token(BaseModel):
    access_token: str
    token_type: str
    expires_in: int
    refresh_token: Optional[str] = None

class TokenRequest(BaseModel):
    username: str
    password: str
    grant_type: str = "password" 