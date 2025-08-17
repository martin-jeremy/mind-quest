from fastapi import FastAPI
from app.core.config import settings
from app.api import users, auth

app = FastAPI(title=settings.APP_NAME, debug=settings.DEBUG)


@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "ok", "message": f"{settings.APP_NAME} is running"}


app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(auth.router, prefix="/auth", tags=["Authenfication"])
