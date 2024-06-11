from fastapi import APIRouter, Request, Depends
from uuid import UUID

from app.db.session import get_db
from app.schemas.crud.client import Client, ClientCreate
from app.crud.clients import crud_create_client

clients_router = r = APIRouter()


@r.post(
    "/clients",
    response_model_exclude_none=True,
)
async def create_client(
    request: Request,
    client: Client,
    db=Depends(get_db),
):
    """
    Create client
    """
    crud_create_client(
        db=db,
        client=ClientCreate(
            first_name=client.first_name, last_name=client.last_name, email=client.email
        ),
    )
