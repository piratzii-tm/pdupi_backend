from fastapi import APIRouter
from src.admin.admin_service import AdminService
from src.calendar_day.calendar_day_model import CalendarDayBase, CalendarDayModel
from src.gym_class.gym_class_model import GymClassBase, GymClassModel
from constants.models.add_class_body import AddClassBody

admin_router = APIRouter(prefix="/admin", tags=["products"])
admin_service = AdminService()


@admin_router.post("/")
async def me():
    print("Implement logic")


@admin_router.get("/")
async def get_admin_by_id(admin_id: int):
    print("Implement logic")


@admin_router.post("/login")
async def login():
    print("Implement logic")


@admin_router.post("/add_trainer")
async def add_trainer():
    print("Implement logic")


@admin_router.post("/add_class")
async def add_class(body: AddClassBody):
    admin_service.add_class(CalendarDayModel(**{
        "day": body.day,
        "month": body.month,
        "starting_hour": body.starting_hour
    }), GymClassModel(**{
        "class_name": body.class_name,
        "instructor_id": body.instructor_id,
        "max_slots": body.max_slots,
        "occupied_slots": body.occupied_slots
    }))
