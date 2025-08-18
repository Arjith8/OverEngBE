PROJECT_NAME = over_engineered

up:
	docker compose -p $(PROJECT_NAME) up -d

down:
	docker compose -p $(PROJECT_NAME) down

build:
	docker compose -p $(PROJECT_NAME) build

logs:
	docker compose -p $(PROJECT_NAME) logs -f

restart: down up

ps:
	docker compose -p $(PROJECT_NAME) ps

shell:
	docker compose -p $(PROJECT_NAME) exec web sh

migrate:
	docker compose -p $(PROJECT_NAME) exec web python manage.py migrate

collectstatic:
	docker compose -p $(PROJECT_NAME) exec web python manage.py collectstatic --noinput

superuser:
	docker compose -p $(PROJECT_NAME) exec web python manage.py createsuperuser

