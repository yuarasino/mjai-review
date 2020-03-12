.PHONY: manage migrate runserver lint format

manage:
	poetry run python src/manage.py ${c}

migrate:
	poetry run python src/manage.py migrate

runserver:
	poetry run python src/manage.py runserver 0.0.0.0:8000

lint:
	poetry run flake8 .

format:
	poetry run black .
	poetry run isort -y
