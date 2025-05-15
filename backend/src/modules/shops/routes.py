from fastapi import APIRouter
from src.repositories.repositories import ShopsRepository

router = APIRouter(prefix="/shops", tags=["Shops"])


@router.get("/")
async def get_all_shops():
    return await ShopsRepository().get_all()


@router.get("/liquidity")
async def get_liquidity():
    pass
