# Teapot API - Django
## Requirements
- Poetry
- Python (v3.10+)
- Docker

## Starting backend server dependencies
The backend depends on Docker containers which run Postgres and Localstack
- Run the containers using the command:
    ```shell
    make start-db
    ```
    - Exit the containers with `CTRL + c`

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
