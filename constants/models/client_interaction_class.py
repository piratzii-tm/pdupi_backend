from pydantic import BaseModel


class ClientInteractionClass(BaseModel):
    client_id: int
    day_id: int
    class_id: int
