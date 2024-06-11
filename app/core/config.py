from pydantic import SecretStr, PostgresDsn
from pydantic_settings import BaseSettings


class PostgresSettings(BaseSettings):
    USER: str
    PASSWORD: SecretStr
    HOST: str = "localhost"
    PORT: int = 5432
    NAME: str

    class Config:
        env_prefix = "DB_"


class Settings(BaseSettings):
    POSTGRES = PostgresSettings()
    POSTGRES_DATABASE_URL: PostgresDsn = PostgresDsn.build(
        scheme="postgresql",
        user=POSTGRES.USER,
        password=POSTGRES.PASSWORD.get_secret_value(),
        host=POSTGRES.HOST,
        port=str(POSTGRES.PORT),
        path=f"/{POSTGRES.NAME}",
    )


settings = Settings()