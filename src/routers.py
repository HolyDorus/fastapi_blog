from fastapi import APIRouter

from src import settings
from src.blog.routes import router as blog_router
from src.user.routes import router as user_router
from src.auth.routes import router as auth_router


main_router = APIRouter(prefix=f'/api/{settings.API_VERSION}')

main_router.include_router(blog_router)
main_router.include_router(user_router)
main_router.include_router(auth_router)
