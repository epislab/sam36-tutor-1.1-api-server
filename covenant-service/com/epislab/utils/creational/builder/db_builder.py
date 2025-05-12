import os
import asyncpg

from com.epislab.utils.creational.builder.query_builder import QueryBuilder
from com.epislab.utils.creational.singleton.db_singleton import db_singleton
from dotenv import load_dotenv
# Async Database Builder
class DatabaseBuilder:
    def __init__(self):
        if not hasattr(db_singleton, "db_url"):
            raise AttributeError("⚠️ db_singleton 인스턴스에 'db_url' 속성이 존재하지 않습니다.")
        
        print(f"✅ Initializing DatabaseBuilder... db_url: {db_singleton.db_url}")  # 디버깅

        self.database_url = db_singleton.db_url
        self.min_size = 1
        self.max_size = 10
        self.timeout = 60
        self.pool = None



    def pool_size(self, min_size: int = 1, max_size: int = 10):
        self.min_size = min_size
        self.max_size = max_size
        return self

    def timeout(self, timeout: int = 60):
        self.timeout = timeout
        return self

    async def build(self):
        if not self.database_url:
            raise ValueError("⚠️ Database URL must be set before building the database")

        print(f"🚀 Connecting to PostgreSQL: {self.database_url}")  # 디버깅

        self.pool = await asyncpg.create_pool(
            dsn=self.database_url,
            min_size=self.min_size,
            max_size=self.max_size,
            timeout=self.timeout,
        )
        return AsyncDatabase(self.pool)

# Async Database Wrapper
class AsyncDatabase:
    def __init__(self, pool):
        self.pool = pool

    async def fetch(self, query: str, *args):
        async with self.pool.acquire() as connection:
            return await connection.fetch(query, *args)

    async def execute(self, query: str, *args):
        async with self.pool.acquire() as connection:
            return await connection.execute(query, *args)

    async def close(self):
        await self.pool.close()



# ✅ 3. FastAPI와 연동을 위한 Database Session Generator
# def get_db():
#     """SQLAlchemy 세션을 제공하는 FastAPI 종속성"""
#     db = session_local()
#     try:
#         yield db
#     finally:
#         db.close()

async def get_db():

    load_dotenv()

    if not hasattr(db_singleton, "db_url") or not db_singleton.db_url:
        print("⚠️ db_singleton이 올바르게 초기화되지 않았습니다. 환경 변수를 다시 로드합니다.")
        db_singleton.db_url = os.getenv("DB_URL")
        
        if not db_singleton.db_url:
            raise AttributeError("❌ 환경 변수를 다시 로드했지만 'db_url'이 설정되지 않았습니다. .env 파일을 확인하세요.")

    print(f"✅ db_singleton 초기화 확인: {db_singleton.db_url}")  # Debug 로그

    builder = DatabaseBuilder()
    db = await builder.build()

    try:
        yield db  # ✅ FastAPI의 Depends()에서 사용할 수 있도록 yield로 반환
    finally:
        await db.close()


# ✅ 4. 초기화 함수 (비동기 DB 테이블 생성)
async def init_db():
    """데이터베이스 초기화"""
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        raise e


# ✅ 5. 사용 예시
if __name__ == "__main__":
    # 🔹 SQLAlchemy DB 설정 빌드
    db_builder = (
        DatabaseBuilder()
        .echo(True)
        .future(True)
        .build()
    )

    engine = db_builder._engine
    session_local = db_builder._session_local
    Base = db_builder._base

    # 🔹 pymysql 쿼리 실행 예시
    query_result = (
        QueryBuilder()
        .connect()
        .query("SELECT * FROM users")
        .execute()
    )
    
    print(f"Query Result: {query_result}")
