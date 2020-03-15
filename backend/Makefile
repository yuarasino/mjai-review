.PHONY: manage migrate runserver

manage:
	poetry run python src/manage.py ${c}

migrate:
	poetry run python src/manage.py migrate

runserver:
	poetry run python src/manage.py runserver 0.0.0.0:8000
