import pytest
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy_utils import database_exists, create_database, drop_database
from fastapi.testclient import TestClient

from app.core.config import settings
from app.db.session import Base, get_db
from app.models.client import Client as ClientModel
from app.models.provider import Provider as ProviderModel
from app.models.provider_schedule import ProviderSchedule as ProviderScheduleModel
from app.main import app


def get_test_db_url() -> str:
    return f"postgresql://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{str(settings.DB_PORT)}/{settings.DB_NAME}_test"


@pytest.fixture(scope="session")
def engine():
    return create_engine(get_test_db_url())


@pytest.fixture(scope="session")
def create_test_db(engine):
    """
    Create a test database and use it for the whole test session.
    """

    test_db_url = get_test_db_url()

    # Create the test database
    assert not database_exists(
        test_db_url
    ), "Test database already exists. Aborting tests."
    create_database(test_db_url)
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)
    drop_database(test_db_url)


@pytest.fixture
def test_db(engine, create_test_db):
    """Returns a sqlalchemy session, and after the test tears down everything properly."""
    connection = engine.connect()
    # begin the nested transaction
    transaction = connection.begin()
    # use the connection with the already started transaction
    session = Session(bind=connection)

    yield session

    session.close()
    # roll back the broader transaction
    transaction.rollback()
    # put back the connection to the connection pool
    connection.close()


@pytest.fixture
def client(test_db):
    """
    Get a TestClient instance that reads/write to the test database.
    """

    def get_test_db():
        yield test_db

    app.dependency_overrides[get_db] = get_test_db

    yield TestClient(app)


@pytest.fixture
def test_client(test_db) -> ClientModel:
    """
    Make a test client in the database
    """
    client = ClientModel(
        email="fake@email.com",
        first_name="test",
        last_name="test",
    )
    test_db.add(client)
    test_db.commit()
    return client


@pytest.fixture
def test_provider(test_db) -> ProviderModel:
    """
    Make a test provider in the database
    """

    provider = ProviderModel(
        email="fake@email.com",
        first_name="test",
        last_name="test",
        specialty="weightloss",
    )
    test_db.add(provider)
    test_db.commit()
    return provider


@pytest.fixture
def test_provider_schedule(test_db, test_provider) -> ProviderScheduleModel:
    """
    Make a test provider schedule in the database
    """
    provider_schedule = ProviderScheduleModel(
        provider_id=test_provider.id,
        is_booked=False,
        start_time=datetime(2024, 6, 30, 8, 0),
        end_time=datetime(2024, 6, 30, 8, 15),
    )
    test_db.add(provider_schedule)
    test_db.commit()
    return provider_schedule
