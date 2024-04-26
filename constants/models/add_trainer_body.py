from pydantic import BaseModel


class AddTrainerBody(BaseModel):
    first_name: str
    last_name: str
