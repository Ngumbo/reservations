def test_create_appointment(client, test_client, test_provider_schedule):
    appointment = {
        "client_id": str(test_client.id),
        "provider_schedule_id": str(test_provider_schedule.id),
    }

    response = client.post(
        f"/api/v1/appointments",
        json=appointment,
    )

    assert response.status_code == 201
    assert test_provider_schedule.is_booked
