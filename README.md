# Teapot API - Django
## Requirements
- Poetry
- Python (v3.10+)
- Docker

## Starting a Postgres DB in a Docker Container
- Pull the Docker image:
    ```
    docker pull postgres:14
    ```
- Start the container:
    ```
    docker run --name some-postgres -e POSTGRES_PASSWORD=password -d -p 5050:5432  postgres:14
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
