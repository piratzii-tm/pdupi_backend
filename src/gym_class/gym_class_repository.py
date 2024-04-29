from database import get_db

from src.gym_class.gym_class_model import GymClassModel
from src.calendar_day.calendar_day_model import CalendarDayModel
from src.instructor.instructor_model import InstructorModel

from constants.models.gym_class_body import GymClassBody

from typing import List


class GymClassRepository:

    def __init__(self):
        self.db = next(get_db())

    def get_gym_class(self, gym_id: int = None, gym_class_body: GymClassBody = None, month: int = None):

        if gym_id:
            response = {
                "class": self.db.query(GymClassModel).where(GymClassModel.id == gym_id).first(),
                "day": self.db.query(CalendarDayModel).where(CalendarDayModel.class_id == gym_id).first()
            }
        elif month:
            days: List[CalendarDayModel] = (self.db.query(CalendarDayModel)
                                            .filter(CalendarDayModel.month == month).all())
            response = []
            for day in days:
                class_in_day: GymClassModel = self.db.query(GymClassModel).where(
                    GymClassModel.id == day.class_id).first()
                instructor: InstructorModel = self.db.query(InstructorModel).where(
                    InstructorModel.id == class_in_day.instructor_id).first()
                response.append({
                    "hour": day.starting_hour,
                    "day": day.day,
                    "day_id": day.id,
                    "class": {
                        "id": class_in_day.id,
                        "class_name": class_in_day.class_name,
                        "occupied_slots": class_in_day.occupied_slots,
                        "max_slots": class_in_day.max_slots,
                        "instructor_name": f"{instructor.last_name} {instructor.first_name[0]}",
                        "instructor_id": instructor.id
                    }})
        elif gym_class_body:
            days: List[CalendarDayModel] = (self.db.query(CalendarDayModel)
                                            .filter(CalendarDayModel.day == gym_class_body.day)
                                            .filter(CalendarDayModel.month == gym_class_body.month).all())
            response = []
            for day in days:
                class_in_day: GymClassModel = self.db.query(GymClassModel).where(
                    GymClassModel.id == day.class_id).first()
                instructor: InstructorModel = self.db.query(InstructorModel).where(
                    InstructorModel.id == class_in_day.instructor_id).first()
                response.append({
                    "hour": day.starting_hour,
                    "day_id": day.id,
                     "class": {
                        "id": class_in_day.id,
                        "class_name": class_in_day.class_name,
                        "occupied_slots": class_in_day.occupied_slots,
                        "max_slots": class_in_day.max_slots,
                        "instructor_name": f"{instructor.last_name} {instructor.first_name[0]}",
                        "instructor_id": instructor.id
                    }
                })
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
