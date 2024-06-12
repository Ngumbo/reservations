# reservations
Reservations api for clients and providers

## Run

### .env setup
Duplicate `.test.env` and name it `.env`. Change the `DB_HOST` to `DB_HOST=postgres`

### Run with docker
```commandline
> sh build.sh
```

### Installing dependencies locally
After creating a python virtual environment, run the following command
```commandline
> poetry install
```

### Running tests
```commandline
> export $(cat .test.env | xargs)
> pytest .
```

### Test Coverage Report
```commandline
> export $(cat .test.env | xargs)
> pytest --cov=app app/tests/
```

## Additional Notes
### Confirming Reservations
To handle this, I would have created a new PATCH endpoint `/api/v1/appointments/{appointment_id}` and as part of the body,
I would send `{"is_confirmed": True}`.

### Reservations must be made at least 24 hours in advance
To handle this, I would add a check on the POST `api/v1/appointments` endpoint to see if the time of creation is 24 hours
before the `provider_schedule` objects start_time. If it is not then I would return a 400 bad request.

### Reservations expire after 30 minutes
To handle this, I would probably use the python library `apsscheduler`. Once an appointment is created, I would create a job
that would trigger after 30 minutes from the time of creation. If the appointment is not yet confirmed, then I would set `provider_schedule`
`is_booked` to False. On the appointment object, I would set `is_expired` to True.

### Trade-offs
One trade off that I had to make to stay within the timeframe is feature development vs adding some tests.
I decided to add some tests for some of the core functionality which slowed down the amount of features that I could complete.
Although, it did slow down the features that I could push out, it did increase test coverage so I at least know that some
of the features that are pushed out are reliable.

I did have to trade-off the robustness of the provider schedule create. Right now, it can only accept a single date, start time,
and end time. There could be cases where a provider might have non-consecutive blocks that they would like to create for a single day (eg. 8-11, 12-3, etc)
right now this would have to be multiple api request while it could just be one.

### Before Production
Before a production deployment, I would definitely like to add a CI/CD pipeline. I would also clean up some of the local docker
environment setup.

Feature wise, I would think through adding timezone consideration. My thought is to add timezone to the provider, so that
their timezone is recorded and when client's book, it can adjust to their timezone.

I would add pagination to the endpoint that gets provider schedules and filtering by day so that, I could pull available
time slots based on the day.

I would also add some form of api authentication.

I would add more edge case checking for the clients and providers endpoint. Right now, those endpoints don't
handle things like duplicate client/providers.

Another thing would be to check if clients can book more than one time slot per day, if not then previous timeslot would
cancel if more than one booking is created per day.
