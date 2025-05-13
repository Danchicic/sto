from logging import getLogger

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from src.core.config import db_config

logger = getLogger(__name__)
DATABASE_URL = f"postgresql+asyncpg://{db_config.database_username}:{db_config.database_password}@{db_config.database_host}:{db_config.database_port}/{db_config.database_name}"
print("DBURL")
print(DATABASE_URL)
engine = create_async_engine(DATABASE_URL, echo=True)
Base = declarative_base()
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def init_models():
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
