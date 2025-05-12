from app.domain.oauth.services.oauth_service import OAuthService

class OAuthController:
    def __init__(self, oauth_service: OAuthService):
        self.oauth_service = oauth_service

    async def create_token(self, username: str, password: str):
        return await self.oauth_service.create_token(username, password) 