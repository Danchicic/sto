from fastapi import APIRouter

router = APIRouter(prefix='/buyers', tags=["Buyers"])


@router.get("/")
async def get_all_buyers():
    pass


@router.get("/with_conditionals")
async def get_buyers_with_conditionals():
    pass


@router.get("/{model}")
async def get_buyers_by_model(model: str):
    pass


@router.post("/buyers")
async def create_buyer():
    pass


@router.delete('/buyers/{id}')
async def delete_buyer(id: int):
    pass
