from database import get_db
from src.gym_class.gym_class_model import GymClassModel
from src.calendar_day.calendar_day_model import CalendarDayModel


class AdminRepository:
    def __init__(self):
        self.db = next(get_db())

    def add_class(self, calendar_day: CalendarDayModel, gym_class: GymClassModel):
        self.db.add(calendar_day)
        self.db.add(gym_class)
        self.db.commit()
