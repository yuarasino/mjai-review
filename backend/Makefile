.PHONY: manage migrate runserver test lint fmt

manage:
	poetry run python src/manage.py ${c}

migrate:
	poetry run python src/manage.py migrate

runserver:
	poetry run python src/manage.py runserver 0.0.0.0:8000

test:
	poetry run pytest tests

test-lf:
	poetry run pytest --lf tests

lint:
	poetry run flake8 .
	poetry run mypy .

fmt:
	poetry run black .
	poetry run isort -y
