from fastapi import APIRouter

gym_class_router = APIRouter(prefix="gym_class", tags=["product"])
#TODO Add gym class service here


@gym_class_router.get("/{id}")
async def get_class_by_id():
    print("Implement logic")


@gym_class_router.get("/all")
async def get_all_classes():
    print("Implement logic")


@gym_class_router.get("/all/year={year}&month={month}")
async def get_class_by_date():
    print("Implement logic")

