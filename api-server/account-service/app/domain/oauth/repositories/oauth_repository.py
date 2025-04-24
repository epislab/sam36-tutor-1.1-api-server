from app.foundation.core.abstraction.repository import BaseRepository
from app.domain.oauth.models.oauth_schema import Token

class OAuthRepository(BaseRepository):
    async def save_token(self, token: Token) -> Token:
        # Implementation for saving token
        pass

    async def get_token(self, token_id: str) -> Token:
        # Implementation for retrieving token
        pass 