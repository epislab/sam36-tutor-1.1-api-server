from enum import Enum

class ManagerAction(Enum):
    
    CREATE_MANAGER = "create_manager"
    DELETE_MANAGER = "delete_manager"
    REMOVE_MANAGER = "remove_manager"
    
    FIND_MANAGERS = "find_managers"
    
    GET_ALL_MANAGERS = "get_all_managers"
    GET_MANAGER_BY_ID = "get_manager_by_id"
    GET_MANAGER_ID = "get_manager_id"
    EXISTS_MANAGER_ID = "exists_manager_id"
    COUNT_MANAGERS = "count_managers"

    
    UPDATE_MANAGER = "update_manager"
    PATCH_MANAGER = "patch_manager"
    