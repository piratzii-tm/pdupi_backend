from database import get_db
from src.client.client_model import ClientModel


class ClientRepository:
    def __init__(self):
        self.db = next(get_db())

    def get_client_by_id(self, received_id: int) -> ClientModel:
        return self.db.query(ClientModel) \
            .filter(ClientModel.id == received_id) \
            .first()

    def get_client_by_email(self, received_email: str) -> ClientModel:
        return self.db.query(ClientModel) \
            .filter(ClientModel.email == received_email) \
            .first()

    def register_client(self, new_user: ClientModel):
        self.db.add(new_user)
        self.db.commit()
