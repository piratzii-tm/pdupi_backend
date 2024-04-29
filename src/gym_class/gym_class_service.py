from src.gym_class.gym_class_repository import GymClassRepository
from constants.models.gym_class_body import GymClassBody


class GymClassService:

    def __init__(self):
        self.gym_class_repository = GymClassRepository()

    def get_gym_class(self, gym_id: int = None, gym_class_body: GymClassBody = None, month: int = None):
        return self.gym_class_repository.get_gym_class(gym_id, gym_class_body,month)
