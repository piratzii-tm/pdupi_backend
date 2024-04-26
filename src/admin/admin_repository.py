from database import get_db
from src.gym_class.gym_class_model import GymClassModel
from src.calendar_day.calendar_day_model import CalendarDayModel
from src.admin.admin_model import AdminModel
from src.instructor.instructor_model import InstructorModel

class AdminRepository:
    def __init__(self):
        self.db = next(get_db())

    def add_class(self, calendar_day: CalendarDayModel, gym_class: GymClassModel):
        self.db.add(calendar_day)
        self.db.add(gym_class)
        self.db.commit()

    def get_admin_by_email(self, received_email: str) -> AdminModel:
        return self.db.query(AdminModel) \
            .filter(AdminModel.email == received_email) \
            .first()

    def add_trainer(self, instructor: InstructorModel):
        self.db.add(instructor)
        self.db.commit()