from src.admin.admin_repository import AdminRepository
from src.gym_class.gym_class_model import GymClassModel
from src.calendar_day.calendar_day_model import CalendarDayModel


class AdminService:
    def __init__(self):
        self.admin_repository = AdminRepository()

    def add_class(self, calendar_day: CalendarDayModel, gym_class: GymClassModel):
        self.admin_repository.add_class(calendar_day, gym_class)
