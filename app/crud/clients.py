from sqlalchemy.orm import Session

from app.models.client import Client as ClientModel
from app.schemas.crud.client import ClientCreate


def crud_create_client(db: Session, client: ClientCreate):
    db_client = ClientModel(
        email=client.email,
        first_name=client.first_name,
        last_name=client.last_name,
    )
    db.add(db_client)
    db.commit()
    db.refresh(db_client)

    return db_client
