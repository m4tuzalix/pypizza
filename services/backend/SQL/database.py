from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = (
    "postgresql+asyncpg://postgres:maniek12@localhost:5433/pypizza"
)

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL, pool_pre_ping=True, echo=True, future=True
)


async def get_session() -> AsyncSession:
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with async_session() as session:
        yield session
