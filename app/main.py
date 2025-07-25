from fastapi import FastAPI
from app.core.config import settings
from app.api import users

app = FastAPI(title=settings.APP_NAME, debug=settings.DEBUG)

app.include_router(users.router, tags=["users"])


@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "ok", "message": f"{settings.APP_NAME} is running"}

