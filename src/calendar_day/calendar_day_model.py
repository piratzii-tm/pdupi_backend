from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from pydantic import BaseModel


class CalendarDayModel(Base):
    __tablename__ = 'calendar_days'

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)

    day = Column(Integer, nullable=False)
    month = Column(Integer, nullable=False)
    starting_hour = Column(Integer, nullable=False)
    class_id = Column(Integer, nullable=False)


class CalendarDayBase(BaseModel):
    day: int
    month: int
    starting_hour: int
    class_id: int
