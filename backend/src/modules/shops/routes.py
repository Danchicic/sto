from fastapi import APIRouter

router = APIRouter(prefix='/shops', tags=["Shops"])


@router.get("/")
async def get_all_shops():
    pass


@router.get('/liquidity')
async def get_liquidity():
    pass
