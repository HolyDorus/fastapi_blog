from fastapi import FastAPI
import uvicorn

from src import settings
from src.routers import main_router


app = FastAPI()

app.include_router(main_router)


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host=settings.APP_HOST,
        port=settings.APP_PORT,
        reload=settings.APP_AUTORELOAD
    )
