from com.epislab.account.auth.login.models.login_action import LoginAction
from com.epislab.auth.web.auth_factory import AuthFactory


class AuthController:
    def __init__(self):
        pass

    def get_stored_refresh_token(self, **kwargs):
        return AuthFactory.create(AuthAction.GET_STORED_REFRESH_TOKEN, **kwargs)
    
    
    def refresh_access_token(self, **kwargs):
        return AuthFactory.create(AuthAction.REFRESH_ACCESS_TOKEN, **kwargs)