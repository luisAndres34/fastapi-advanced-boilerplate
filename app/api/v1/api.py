from fastapi import APIRouter

from . import auth, users

api_router = APIRouter()

# Here we group all our v1 endpoints
api_router.include_router(auth.router)
api_router.include_router(users.router)
