import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from src.core.redis_initializer import close_redis, init_redis
from src.database import init_models
from src.routes import main_router
from starlette.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    await init_models()
    await init_redis()
    yield
    await close_redis()


app = FastAPI(
    lifespan=lifespan,
)
app.include_router(main_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost", "http://localhost:80"],
    allow_credentials=True,
    allow_methods=["*"],
)
