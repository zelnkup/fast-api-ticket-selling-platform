build:
	docker-compose build

run:
	docker-compose up

shell:
	docker-compose run --rm web python manage.py shell

bash:
	docker-compose run --rm web alembic init alembic

migrations:
	docker-compose run --rm web alembic revision --autogenerate

migrate:
	docker-compose run --rm web alembic upgrade head

hooks_setup:
	pip install black flake8 isort[pyproject] pre-commit
	pre-commit install
