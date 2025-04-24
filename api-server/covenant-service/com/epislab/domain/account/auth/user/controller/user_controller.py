from com.epislab.account.auth.user.api.user_factory import UserFactory
from com.epislab.account.auth.user.models.user_action import UserAction


class UserController:
    def __init__(self):
        pass

    async def create_new_user(self, **kwargs):
        return await UserFactory.create(UserAction.CREATE_NEW_USER, **kwargs)
    
    async def login(self, **kwargs):
        return await UserFactory.create(UserAction.LOGIN, **kwargs)
    
    async def logout(self, **kwargs):
        return await UserFactory.create(UserAction.LOGOUT, **kwargs)
    
    
    
    

   