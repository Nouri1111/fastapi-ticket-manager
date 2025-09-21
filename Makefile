# Variables
APP_NAME = fastapi-ticket-manager
PYTHON = python
PIP = pip
UVICORN = uvicorn
PYTEST = pytest
RUFF = ruff
DOCKER = docker
VENV_ACTIVATE = . venv/bin/activate &&  # Command to activate the virtual environment

# Default target
.DEFAULT_GOAL := help

# Help target
help:
	@echo "Available commands:"
	@echo "  make install       Install dependencies"
	@echo "  make run           Run the FastAPI application"
	@echo "  make test          Run unit tests with pytest"
	@echo "  make lint          Check code quality with ruff"
	@echo "  make lint-fix      Auto-fix linting issues with ruff"
	@echo "  make build         Build the Docker image"
	@echo "  make clean         Clean up temporary files"

# Install dependencies
install:
	@if [ ! -d "venv" ]; then \
		echo "Creating virtual environment..."; \
		$(PYTHON) -m venv venv; \
	fi
	@echo "Activating virtual environment and installing dependencies..."
	$(VENV_ACTIVATE) $(PIP) install -r requirements.txt

# Run the application
run:
	$(VENV_ACTIVATE) $(UVICORN) app.main:app --reload

# Run tests
test:
	$(VENV_ACTIVATE) $(PYTEST) --cov=app --cov-report=term-missing

# Lint code
lint:
	$(VENV_ACTIVATE) $(RUFF) app/ tests/

# Auto-fix linting issues
lint-fix:
	$(VENV_ACTIVATE) $(RUFF) app/ tests/ --fix

# Build Docker image
build:
	$(DOCKER) build -t $(APP_NAME) .

# Clean up temporary files
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf .pytest_cache .ruff_cache htmlcov