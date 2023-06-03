build:
	docker compose -f docker-compose.yml create

start-db:
	docker compose up

runserver:
	python manage.py runserver

stop:
	docker compose stop