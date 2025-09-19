# Makefile for common tasks

install:
	pip install -r requirements.txt

run:
	uvicorn app.main:app --reload

test:
	pytest --cov=app tests/

lint:
	ruff app/ tests/

format:
	ruff app/ tests/ --fix

build:
	docker build -t fastapi-ticket-manager .

run-docker:
	docker run -p 8000:8000 fastapi-ticket-manager