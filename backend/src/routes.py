from fastapi import APIRouter
from src.modules.buyers.routes import router as buyer_router
from src.modules.cars.routes import router as cars_router
from src.modules.shops.routes import router as shop_router

main_router = APIRouter()
main_router.include_router(buyer_router)
main_router.include_router(shop_router)
main_router.include_router(cars_router)


@main_router.get("/health")
async def health_check():
    return {"status": "ok"}
