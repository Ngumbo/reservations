from fastapi import APIRouter, Request, Depends

from app.db.session import get_db
from app.schemas.crud.providers import Provider, ProviderCreate
from app.crud.providers import crud_create_provider

providers_router = r = APIRouter()


@r.post(
    "/providers",
    response_model_exclude_none=True,
    status_code=201
)
async def create_provider(
    request: Request,
    provider: Provider,
    db=Depends(get_db),
):
    """
    Create provider
    """
    created_provider = crud_create_provider(
        db=db,
        provider=ProviderCreate(
            first_name=provider.first_name,
            last_name=provider.last_name,
            email=provider.email,
            specialty=provider.specialty,
        ),
    )

    return {"provider_id": created_provider.id}
