from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker, mapped_column, Mapped
from src.core.config import db_config
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.pool import NullPool
DATABASE_URL = f"postgresql+asyncpg://{db_config.database_username}:{db_config.database_password}@{db_config.database_host}:{db_config.database_port}/{db_config.database_name}"

engine = create_async_engine(DATABASE_URL, echo=True, poolclass=NullPool)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)


async def init_models():
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
