from fastapi import APIRouter

gym_class_router = APIRouter(prefix="/gym_class", tags=["product"])
# TODO Add gym class service here


@gym_class_router.get("/")
async def get_class_by_id(id: int):
    print("Implement logic")


@gym_class_router.get("/all")
async def get_all_classes():
    print("Implement logic")


@gym_class_router.get("/filtered")
async def get_class_by_date(year: int, month: int):
    print("Implement logic")
