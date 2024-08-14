from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
import redis

from config import POSTGRES_HOST, POSTGRES_NAME, POSTGRES_PASSWORD, POSTGRES_PORT, POSTGRES_USER, REDIS_HOST, REDIS_PORT


redis_connection_pool = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT, db=0)

DATABASE_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_NAME}"

class Base(DeclarativeBase):
    pass

async_engine = create_async_engine(
    DATABASE_URL, 
    echo=False
)

sessionmaker = async_sessionmaker(async_engine, expire_on_commit=False)


print(DATABASE_URL)