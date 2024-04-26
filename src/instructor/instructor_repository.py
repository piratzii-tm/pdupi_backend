from database import get_db
from src.instructor.instructor_model import InstructorModel


class InstructorRepository:
    def __init__(self):
        self.db = next(get_db())

    def get_instructor(self, instructor_id: int = None):

        if instructor_id:
            return self.db.query(InstructorModel).where(InstructorModel.id == instructor_id).first()
        else:
            return self.db.query(InstructorModel).all()
