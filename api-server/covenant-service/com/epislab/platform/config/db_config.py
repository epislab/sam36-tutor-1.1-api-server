import os
import asyncio
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 환경 변수 로드
load_dotenv()

# ✅ 1. 환경 변수에서 DB URL 가져오기
# 환경 변수 가져오기
DB_HOSTNAME = os.getenv("DB_HOSTNAME", "localhost")
DB_USERNAME = os.getenv("DB_USERNAME", "user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_DATABASE = os.getenv("DB_DATABASE", "mydatabase")

# PostgreSQL `DB_URL` 생성
DATABASE_URL = f"postgresql+asyncpg://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOSTNAME}:{DB_PORT}/{DB_DATABASE}"

if not DATABASE_URL:
    raise ValueError("❌ 환경 변수 'DB_URL'이 설정되지 않았습니다.")
else:
    print("✅😁😁😁😁 DB_URL 환경 변수가 설정되었습니다.")

# ✅ 2. SQLAlchemy 비동기 엔진 설정 (asyncpg 사용)
engine = create_async_engine(
    DATABASE_URL,
    echo=True,          # SQL 실행 로그 표시 (디버깅용)
    future=True,        # 최신 SQLAlchemy API 사용
    pool_size=5,        # 커넥션 풀 크기 설정
    max_overflow=10,    # 최대 오버플로우 커넥션 개수
    pool_timeout=30,    # 커넥션 대기 시간 (초)
    pool_recycle=1800,  # 커넥션 재활용 시간 (초)
)

# ✅ 3. 세션 팩토리 생성
async_session_maker = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# ✅ 4. 데이터베이스 모델 정의
Base = declarative_base()

# ✅ 5. FastAPI에서 사용할 비동기 DB 세션 제공 함수
async def get_db():
    async with async_session_maker() as session:
        yield session  # FastAPI의 Depends()에서 사용 가능

# ✅ 6. 비동기 테이블 생성 함수
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# ✅ 7. FastAPI 실행 시 DB 초기화
if __name__ == "__main__":
    asyncio.run(init_db())  # 초기화 실행
    print("✅ Database initialized successfully!")
