from fastapi import APIRouter

from src.modules.sto.routes import router as sto_router

main_router = APIRouter()
main_router.include_router(sto_router)
