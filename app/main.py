from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(title=settings.APP_NAME, debug=settings.DEBUG)


@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "ok", "message": f"{settings.APP_NAME} is running"}
