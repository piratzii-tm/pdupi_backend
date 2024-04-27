from pydantic import BaseModel


class GymClassBody(BaseModel):
    day: str
    month: str
