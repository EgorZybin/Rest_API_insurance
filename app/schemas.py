from pydantic import BaseModel


class RateBase(BaseModel):
    cargo_type: str
    rate: float


class RateCreate(RateBase):
    date: str


class RateOut(BaseModel):
    id: str
    date: str
    cargo_type: str
    rate: float

    class Config:
        from_attributes = True
