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
