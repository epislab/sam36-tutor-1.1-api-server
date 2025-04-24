from sqlalchemy.engine import Result, Row
from com.epislab.account.auth.user.repositories.find_user import build_check_email_stmt, build_login_stmt
from com.epislab.utils.config.security.jwt_config import create_access_token, create_refresh_token
from com.epislab.utils.creational.abstract.abstract_service import AbstractService
from com.epislab.utils.config.security.redis_config import redis_client

class Login(AbstractService):
    async def handle(self, **kwargs):
        print("😁😁😁😁Login 진입함")
        user_schema = kwargs.get("user_schema")
        db = kwargs.get("db")
        print("🐍🐍🐍🐍user_schema : ", user_schema)
        # user_schema는 dict 또는 객체라고 가정
        # user_schema는 dict 또는 Pydantic 모델
        user_dict = user_schema.dict()

        email = user_dict.get("email")
        password = user_dict.get("password")

        # 1단계: user_id 존재 여부 확인
        check_email_stmt, params = build_check_email_stmt(email)
        check_email_result: Result = await db.execute(check_email_stmt, params)
        fetched_email: Row | None = check_email_result.fetchone()
        if fetched_email is None:
            return {
                "message": "등록된 Email 이 없습니다",
                "logged_in_user": {}
            }
        
        login_stmt, params = build_login_stmt(email, password)
        login_result: Result = await db.execute(login_stmt, params)
        fetched_user: Row | None = login_result.fetchone()

        if fetched_user is None:
            return {
                "message": "비밀번호가 일치하지 않습니다",
                "logged_in_user": {}
            }
        
        # access_token 생성, refresh_token 생성

        logged_in_user: dict = dict({"user_id": fetched_user.user_id})
        
        access_token = create_access_token(logged_in_user)
        refresh_token = create_refresh_token(logged_in_user)
        print("🔑🔑🔑🔑🔑😁😁😁😁access_token : ", access_token)
        print("🩻🩻🩻🩻🩻🤗🤗🤗🤗🤗🤗refresh_token : ", refresh_token)
        # ✅ Redis에 refresh_token 저장
        user_id = logged_in_user.get("user_id")
        await redis_client.set(
            name=f"refresh_token:{user_id}", 
            value=refresh_token, 
            ex=60 * 60 * 24 * 7  # 7일 (만료 시간 설정)
        )
        return {
            "message": "SUCCESS",
            "logged_in_user": logged_in_user,
            "access_token": access_token,
            "refresh_token": refresh_token
        }
            
            





        

