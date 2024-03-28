from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base


class ReservationModel(Base):
    __tablename__ = 'reservations'

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)

    client_id = Column(Integer, ForeignKey("clients.id"), primary_key=True)
    class_id = Column(Integer, ForeignKey("gym_classes.id"), primary_key=True)
    day_id = Column(Integer, ForeignKey("calendar_days.id"), primary_key=True)


class ReservationBase:
    client_id: int
    class_id: int
    day_id: int
