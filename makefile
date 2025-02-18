run-server:
	PYTHONPATH=src uvicorn --reload main:app --host 0.0.0.0 --port 8000

db-init:
	PYTHONPATH=src alembic init migrations

db-migrate:
	PYTHONPATH=src alembic revision --autogenerate
	PYTHONPATH=src alembic upgrade head

db-upgrade:
	PYTHONPATH=src alembic upgrade head

db-prestart:
	PYTHONPATH=src python ./src/initial_data.py


run-test:
ifdef dst
	PYTHONPATH=src python -m pytest $(dst) -v
else
	PYTHONPATH=src python -m pytest -v
endif