from pydantic import BaseModel


class Provider(BaseModel):
    first_name: str
    last_name: str
    email: str
    specialty: str


class ProviderCreate(Provider):
    pass
