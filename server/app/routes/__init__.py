from fastapi import APIRouter
from .user_routes import router as user_router
from .medication_routes import router as medication_router

router = APIRouter()
router.include_router(user_router, prefix="/users", tags=["users"])
router.include_router(medication_router, prefix="/medications", tags=["medications"])