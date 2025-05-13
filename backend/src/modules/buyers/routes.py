from fastapi import APIRouter, Depends

from src.repositories.repositories import BuyersRepository

from . import schemas
from .depends import get_buyers_conditionals

router = APIRouter(prefix="/buyers", tags=["Buyers"])


@router.get(
    "/",
    response_model=schemas.Buyers,
)
async def get_all_buyers():
    return {"buyers": await BuyersRepository().get_all()}


@router.get("/with_conditionals")
async def get_buyers_with_conditionals(
        conditionals: schemas.BuyersConditionals = Depends(get_buyers_conditionals),
):
    return {
        "buyers": await BuyersRepository().get_values_by_conditionals(
            conditionals.model_dump()
        )}


@router.get("/{model}")
async def get_buyers_by_model(model_id: int):
    await BuyersRepository().get_buyers_by_model(model_id)


@router.post("/")
async def create_buyer(buyer: schemas.BuyerCreate) -> schemas.Buyer:
    return await BuyersRepository().add_one(buyer.model_dump())


@router.delete("/{id}")
async def delete_buyer(id: int):
    await BuyersRepository().delete_by_id(id=id)
