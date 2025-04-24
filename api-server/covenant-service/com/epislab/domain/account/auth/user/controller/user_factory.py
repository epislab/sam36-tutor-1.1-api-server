from com.epislab.account.auth.user.models.user_action import UserAction
from com.epislab.account.auth.user.services.user_lookup import Login
from com.epislab.account.auth.user.services.user_mutation import CreateNewUser


class UserFactory:
    
    _strategy_map = {
        

    UserAction.CREATE_NEW_USER: CreateNewUser(),
    UserAction.LOGIN: Login(),

    }

    @staticmethod
    async def create(strategy, **kwargs):
        instance = UserFactory._strategy_map[strategy]
        if not instance:
            raise Exception("invalid strategy")
        return await instance.handle(**kwargs)