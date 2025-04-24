from com.epislab.account.auth.user.models.user_entity import UserEntity
from com.epislab.account.auth.user.models.user_schema import UserSchema

async def build_create_new_user(new_user: UserSchema):

    return UserEntity(
        user_id=new_user.user_id,
        email=new_user.email,
        password=new_user.password, 
        name=new_user.name,
    )
    
