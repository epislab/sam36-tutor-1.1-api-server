from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.oauth.oauth_router import router as oauth_router

app = FastAPI(
    title="Auth Service",
    description="OAuth Authentication Service",
    version="1.0.0"
)

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(oauth_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Welcome to Auth Service"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    ) 