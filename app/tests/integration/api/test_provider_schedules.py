from datetime import datetime
from app.domain.provider_schedules import create_schedule


def test_create_provider_schedule(client, test_provider, test_db):
    schedule = {
        "schedule_date": "2024-06-11",
        "start_time_hour": 8,
        "start_time_minute": 0,
        "end_time_hour": 9,
        "end_time_minute": 0,
    }

    response = client.post(
        f"/api/v1/provider_schedules/{str(test_provider.id)}",
        json=schedule,
    )

    assert response.status_code == 201


def test_create_provider_schedule_failure(client, test_provider, test_db):
    schedule = {
        "schedule_date": "2024-06-11",
        "start_time_hour": 8,
        "start_time_minute": 0,
        "end_time_hour": 7,
        "end_time_minute": 0,
    }

    response = client.post(
        f"/api/v1/provider_schedules/{str(test_provider.id)}",
        json=schedule,
    )

    assert response.status_code == 400


def test_get_provider_schedule(client, test_provider, test_db):
    start_time = datetime(2024, 6, 30, 8, 0)
    end_time = datetime(2024, 6, 30, 9, 0)
    create_schedule(
        db=test_db,
        provider_id=test_provider.id,
        start_time=start_time,
        end_time=end_time,
    )
    response = client.get(
        f"/api/v1/provider_schedules/{str(test_provider.id)}",
    )

    assert response.status_code == 200
    assert len(response.json()["items"]) == 4
