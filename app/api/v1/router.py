from fastapi import APIRouter, Depends
from app.api.v1.users import router as users_router
from app.api.v1.auth import router as auth_router
from app.api.deps import get_current_user

api_router = APIRouter()

api_router.include_router(auth_router, prefix="/auth", tags=["auth"])

api_router.include_router(users_router, prefix='/users', tags=['users'], dependencies=[Depends(get_current_user)])

