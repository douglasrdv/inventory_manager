.PHONY: install
install:
	poetry install

.PHONY: migrate
migrate:
	poetry run python -m deliriosmanager.manage migrate

.PHONY: migrations
migrations:
	poetry run python -m deliriosmanager.manage makemigrations

.PHONY: run-server
run-server:
	poetry run python -m deliriosmanager.manage runserver

.PHONY: superuser
superuser:
	poetry run python -m deliriosmanager.manage createsuperuser

.PHONY: update
update: install migrate ;