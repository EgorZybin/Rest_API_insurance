import uuid

from sqlalchemy import Column, Float, String, Date, UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Rate(Base):
    __tablename__ = 'rates'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    cargo_type = Column(String)
    rate = Column(Float)
    date = Column(Date)
