from pydantic import BaseModel


class AddClassBody(BaseModel):
    class_name: str
    instructor_id: int
    max_slots: int
    occupied_slots: int
    day: int
    month: int
    starting_hour: int
