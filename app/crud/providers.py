from sqlalchemy.orm import Session

from app.models.provider import Provider as ProviderModel
from app.schemas.crud.providers import ProviderCreate


def crud_create_provider(db: Session, provider: ProviderCreate):
    db_provider = ProviderModel(
        email=provider.email,
        first_name=provider.first_name,
        last_name=provider.last_name,
        specialty=provider.specialty,
    )
    db.add(db_provider)
    db.commit()
    db.refresh(db_provider)

    return db_provider
