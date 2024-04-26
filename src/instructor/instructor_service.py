from src.instructor.instructor_repository import InstructorRepository

class InstructorService:
    def __init__(self):
        self.instructor_repository = InstructorRepository()

    def get_instructor(self, instructor_id: int = None):
        return self.instructor_repository.get_instructor(instructor_id)