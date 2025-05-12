from com.epislab.account.user.service.hello_user import HelloUser

strategy_map = {
    "hello_user": HelloUser(),
}

class UserFactory:

    @staticmethod
    def create(strategy, **kwargs):
        instance = strategy_map[strategy]
        if not instance:
            raise Exception("invalid strategy")
        return instance.handle(**kwargs)