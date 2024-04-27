from database import get_db

from src.gym_class.gym_class_model import GymClassModel
from src.calendar_day.calendar_day_model import CalendarDayModel

from constants.models.gym_class_body import GymClassBody


class GymClassRepository:

    def __init__(self):
        self.db = next(get_db())

    def get_gym_class(self, gym_id: int = None, gym_class_body: GymClassBody = None):

        if gym_id:
            response = {
                "class": self.db.query(GymClassModel).where(GymClassModel.id == gym_id).first(),
                "day": self.db.query(CalendarDayModel).where(CalendarDayModel.class_id == gym_id).first()
            }
        elif gym_class_body:
            day: CalendarDayModel = (self.db.query(CalendarDayModel)
                                     .filter(CalendarDayModel.day == gym_class_body.day)
                                     .filter(CalendarDayModel.month == gym_class_body.month).first())
            response = self.db.query(GymClassModel).where(GymClassModel.id == day.class_id).all()
        else:
            response = []
            gym_classes = self.db.query(GymClassModel).all()
            for one_gym_class in gym_classes:
                days = self.db.query(CalendarDayModel).where(CalendarDayModel.class_id == one_gym_class.id)
                for day in days:
                    response.append(
                        {
                            "class": one_gym_class,
                            "day": day
                        }
                    )

        return response
