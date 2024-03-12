run-server:
	PYTHONPATH=src uvicorn --reload main:app --host 0.0.0.0 --port 8000

db-init:
	PYTHONPATH=src alembic init migrations

db-migrate:
	PYTHONPATH=src alembic revision --autogenerate
	PYTHONPATH=src alembic upgrade head

db-upgrade:
	PYTHONPATH=src alembic upgrade head