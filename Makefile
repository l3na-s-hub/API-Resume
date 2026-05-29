.PHONY: install run migrate seed test clean

install:
	pip install -r requirements.txt

run:
	uvicorn app.main:app --reload --port 8000

migrate:
	alembic upgrade head

seed:
	python scripts/seed_data.py

test:
	pytest tests/ -v

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
