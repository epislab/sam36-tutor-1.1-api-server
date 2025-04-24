

from com.epislab.account.employee.manager.api.manager_factory import ManagerFactory
from com.epislab.account.employee.manager.models.manager_action import ManagerAction

class ManagerController:
    def __init__(self):
        pass

    async def create_manager(self, **kwargs):
        return await ManagerFactory.create(ManagerAction.CREATE_NEW_USER, **kwargs)

    async def delete_manager(self, **kwargs):
        return await ManagerFactory.create(ManagerAction.DELETE_USER,  **kwargs)
    
    async def count_managers(self, **kwargs):
        return await ManagerFactory.create(ManagerAction.COUNT_USERS, **kwargs)

    async def get_manager_id(self, **kwargs):
        return await ManagerFactory.create(ManagerAction.GET_USER_ID, **kwargs)
