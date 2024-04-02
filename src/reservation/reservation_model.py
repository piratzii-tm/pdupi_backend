from sqlalchemy import Column, Integer, ForeignKey
from database import Base
from pydantic import BaseModel


class ReservationModel(Base):
    __tablename__ = 'reservations'

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)

    client_id = Column(Integer, ForeignKey("client.id"))
    class_id = Column(Integer, ForeignKey("gym_classes.id"))
    day_id = Column(Integer, ForeignKey("calendar_days.id"))


class ReservationBase(BaseModel):
    client_id: int
    class_id: int
    day_id: int
