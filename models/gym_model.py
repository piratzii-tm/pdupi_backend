from sqlalchemy import Column, Integer, String, Float
from database import Base
from sqlalchemy.orm import relationship
from pydantic import BaseModel


class GymModel(Base):
    __tablename__ = 'gyms'

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100))
    address = Column(String(100))
    opening = Column(String(100))
    closing = Column(String(100))
    price = Column(Float)
    max_clients_accepted = Column(Integer)
    current_number_of_clients = Column(Integer)

    workers = relationship("WorkerModel", back_populates="gym")


class GymBase(BaseModel):
    id: int
    name: str
    address: str
    opening: str
    closing: str
    price: float
    max_clients_accepted: int
    current_number_of_clients: int
    workers: list[int] = []
