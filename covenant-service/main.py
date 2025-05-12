from dotenv import load_dotenv
from fastapi import Depends, FastAPI
from fastapi.responses import HTMLResponse
from contextlib import asynccontextmanager

from com.epislab.app_router import router as app_router
from fastapi.middleware.cors import CORSMiddleware  

load_dotenv()


# ✅ FastAPI 애플리케이션 생성
app = FastAPI()
# ✅ CORS 설정 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 🔥 모든 도메인에서 요청 허용 (보안상 필요하면 특정 도메인만 허용)
    allow_credentials=True,
    allow_methods=["*"],  # ✅ 모든 HTTP 메서드 허용 (POST, OPTIONS 등)
    allow_headers=["*"],  # ✅ 모든 헤더 허용
)

# ✅ 애플리케이션 시작 시 `init_db()` 실행
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀🚀🚀🚀 FastAPI 앱이 시작됩니다. 데이터베이스 초기화 중...")
    # await init_db()  # ✅ DB 초기화 실행
    # print("✅ 데이터베이스 초기화 완료!")
    yield  # 애플리케이션이 실행되는 동안 유지
    print("🛑 FastAPI 앱이 종료됩니다.")
    await engine.dispose()  # 🔥 모든 커넥션 정리
    print("✅ DB 연결이 정상적으로 종료되었습니다.")

# ✅ 라우터 등록
app.include_router(app_router, prefix="/api")

def current_time():
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@app.get(path="/")
async def home():
    return HTMLResponse(content=f"""
<body>
<div style="width: 400px; margin: 50 auto;">
    <h1> 현재 서버 구동 중입니다.</h1>
    <h2>{current_time()}</h2>
</div>
</body>
""")

    

