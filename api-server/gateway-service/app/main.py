from fastapi import FastAPI, APIRouter, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import httpx
from typing import Dict, Any
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI(
    title="Gateway API",
    description="Gateway API Service",
    version="1.0.0"
)

# Create API Router with prefix
api_router = APIRouter(prefix="/api")

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# AUTH service URL from environment variable
AUTH_SERVICE_URL = os.getenv("AUTH_SERVICE_URL")

if not AUTH_SERVICE_URL:
    raise ValueError("AUTH_SERVICE_URL environment variable is not set")

@api_router.get("/")
async def root():
    return {"message": "Welcome to Gateway API"}

@api_router.post("/auth/tokens")
async def receive_tokens(tokens: Dict[str, Any]):
    try:
        # Here you can add logic to store or process the tokens
        # For now, we'll just return a success response
        return {
            "status": "SUCCESS",
            "message": "Tokens received successfully"
        }
    except Exception as e:
        return {
            "status": "ERROR",
            "message": f"Failed to process tokens: {str(e)}"
        }

@api_router.api_route("/auth/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def proxy_to_auth(request: Request, path: str):
    # Get the full URL path
    url = f"{AUTH_SERVICE_URL}/{path}"
    
    # Get query parameters
    query_params = dict(request.query_params)
    
    # Get request body if exists
    body = None
    if request.method in ["POST", "PUT"]:
        try:
            body = await request.json()
        except:
            body = None
    
    # Forward headers
    headers = dict(request.headers)
    # Remove host header to avoid conflicts
    headers.pop("host", None)
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.request(
                method=request.method,
                url=url,
                params=query_params,
                json=body,
                headers=headers,
                timeout=30.0
            )
            return response.json()
        except httpx.HTTPError as e:
            raise HTTPException(status_code=500, detail=f"Error connecting to auth service: {str(e)}")

# Include the router in the main app
app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8080,
        reload=True
    ) 