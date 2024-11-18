import uuid
from datetime import datetime

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
import os
from app.models import Base, Rate
import json
import asyncio

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_async_engine(DATABASE_URL, future=True, echo=True)
async_session = async_sessionmaker(engine,
                                   class_=AsyncSession,
                                   expire_on_commit=False)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def load_initial_data():
    async with async_session() as db:

        with open("app/rates.json") as f:
            rates = json.load(f)

        # Заполнение таблицы
        for date, rates_list in rates.items():
            for rate in rates_list:
                insurance_rate = Rate(
                    id=uuid.uuid4(),
                    cargo_type=rate['cargo_type'],
                    rate=float(rate['rate']),
                    date=datetime.strptime(date, '%Y-%m-%d').date()
                )
                db.add(insurance_rate)

        await db.commit()


async def main():
    await init_db()
    await load_initial_data()


if __name__ == "__main__":
    asyncio.run(main())
