from fastapi import APIRouter, HTTPException
from sqlalchemy.future import select
from app.database import async_session
from app.models import Rate
from app.schemas import RateCreate, RateOut
from datetime import datetime

router = APIRouter()


@router.post("/rates/", response_model=RateOut)
async def create_rate(rate: RateCreate):
    date_obj = datetime.strptime(rate.date, "%Y-%m-%d").date()
    async with async_session() as session:
        async with session.begin():
            new_rate = Rate(cargo_type=rate.cargo_type, rate=rate.rate, date=date_obj)
            session.add(new_rate)
        return {
            "id": str(new_rate.id),
            "date": new_rate.date.isoformat(),
            "cargo_type": new_rate.cargo_type,
            "rate": new_rate.rate,
        }


@router.get("/insurance/{cargo_type}/{value}/{date}")
async def calculate_insurance(cargo_type: str, value: float, date: str):
    date_obj = datetime.strptime(date, "%Y-%m-%d").date()
    async with async_session() as session:
        async with session.begin():
            result = await session.execute(
                select(Rate).where(Rate.cargo_type == cargo_type, Rate.date <= date_obj).order_by(Rate.date.desc()))
            rate = result.scalars().first()
            if not rate:
                raise HTTPException(status_code=404, detail="Rate not found")
            insurance_cost = value * rate.rate
    return {"insurance_cost": insurance_cost}
