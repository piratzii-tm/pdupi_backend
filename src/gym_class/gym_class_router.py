from fastapi import APIRouter
from src.gym_class.gym_class_service import GymClassService
from constants.models.gym_class_body import GymClassBody

gym_class_router = APIRouter(prefix="/gym_class", tags=["product"])
gym_class_service = GymClassService()


@gym_class_router.get("/")
async def get_class_by_id(gym_id: int):
    return gym_class_service.get_gym_class(gym_id=gym_id)


@gym_class_router.post("/all")
async def get_all_classes():
    return gym_class_service.get_gym_class()



@gym_class_router.post("/filtered")
async def get_class_by_date(body: GymClassBody):
    return gym_class_service.get_gym_class(gym_class_body=body)
