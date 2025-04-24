from sqlalchemy.ext.asyncio import AsyncSession
from com.epislab.utils.creational.abstract.abstract_service import AbstractService
from com.epislab.account.auth.user.models.user_schema import UserSchema
from sqlalchemy.ext.asyncio import AsyncSession
from com.epislab.utils.creational.abstract.abstract_service import AbstractService
from com.epislab.account.auth.user.repositories.mutate_user import build_create_new_user

class CreateNewUser(AbstractService):

    async def handle(self, **kwargs):
        db: AsyncSession = kwargs.get("db")
        new_user: UserSchema = kwargs.get("new_user")
        try:
            user = await build_create_new_user(new_user)
            db.add(user)
            await db.commit()
            await db.refresh(user)
            return user
        except Exception as e:
            print(f"[ERROR] UserCreate failed: {e}")
            await db.rollback()
            raise e


