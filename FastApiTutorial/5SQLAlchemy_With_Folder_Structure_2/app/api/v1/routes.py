from fastapi import APIRouter
from app.controllers import user_controller, post_controller

api_router = APIRouter()
api_router.include_router(user_controller.router, prefix="/auth", tags=["Users"])
api_router.include_router(post_controller.router, prefix="/posts", tags=["Posts"])
