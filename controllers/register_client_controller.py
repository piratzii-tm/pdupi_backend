from models.client_model import ClientModel, ClientBase
from sqlalchemy.orm import Session
from services import register_client_service


def register_client(client_data: ClientBase, database: Session):
    client = register_client_service.register_client(ClientModel(**client_data.dict()))
    database.add(client)
    database.commit()

