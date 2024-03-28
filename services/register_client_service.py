from models.client_model import ClientModel


def register_client(client: ClientModel) -> ClientModel:
    client.first_name = "Iulian"
    return client
