# Teapot API - Django
## Requirements
- Poetry
- Python (v3.10+)
- Docker

## Starting a Postgres DB in a Docker Container
- Create the containers:
    ```
    make build
    ```
- Start the containers:
    ```
    make start
    ```
- Stop the containers:
    ```
    make stop
    ```

## Installing Dependencies
```
poetry install
```

## Activate Python Virtual Environment
```
poetry shell
```
- Exit with
    ```
    exit
    ```

## Applying Database Migrations
```
python manage.py migrate
```

## Running the API Locally
```
python manage.py runserver
```
