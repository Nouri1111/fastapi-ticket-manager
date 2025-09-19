# FastAPI Ticket Manager

## Overview
This project is a FastAPI-based backend application for managing tickets. It includes features such as creating, updating, listing, and closing tickets. The application follows a clean, layered architecture and uses SQLite as the default database.

## Features
- **Endpoints**:
  - `POST /tickets/`: Create a new ticket.
  - `GET /tickets/`: List all tickets.
  - `GET /tickets/{ticket_id}`: Retrieve a ticket by ID.
  - `PUT /tickets/{ticket_id}`: Update a ticket.
  - `PATCH /tickets/{ticket_id}/close`: Close a ticket.
- **Middleware**: Logs execution time for each request.
- **Swagger Documentation**: Auto-generated at `/docs`.
- **Unit Tests**: Includes pytest tests with ≥80% coverage.
- **Test Coverage**: Easily check test coverage using `pytest-cov`.

## Requirements
- Python 3.10+
- FastAPI
- Uvicorn
- SQLite (default database)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Nouri1111/fastapi-ticket-manager.git
   cd fastapi-ticket-manager
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application
1. Start the FastAPI server:
   ```bash
   uvicorn app.main:app --reload
   ```

2. Access the application:
   - API: [http://127.0.0.1:8000](http://127.0.0.1:8000)
   - Swagger Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Running Tests
Run the unit tests using pytest:
```bash
pytest --cov=app --cov-report=term-missing
```

### Complete Command-Line Examples for Running Tests
1. **Run all tests**:
   ```bash
   pytest
   ```

2. **Run tests with coverage report**:
   ```bash
   pytest --cov=app --cov-report=term-missing
   ```

3. **Run a specific test file**:
   ```bash
   pytest tests/test_tickets.py
   ```

4. **Run a specific test function**:
   ```bash
   pytest tests/test_tickets.py::test_create_ticket
   ```

5. **Run tests with detailed output**:
   ```bash
   pytest -v
   ```

6. **Run tests and stop on the first failure**:
   ```bash
   pytest -x
   ```

7. **Run tests with a minimum coverage threshold**:
   ```bash
   pytest --cov=app --cov-report=term-missing --cov-fail-under=80
   ```

## Project Structure
```
app/
  ├── main.py                # Application entrypoint
  ├── core/                  # Middleware and utilities
  │     └── middleware.py    # Profiling middleware
  ├── db/                    # Database engine and session
  │     └── base.py
  ├── models/                # SQLAlchemy models
  │     └── ticket.py
  ├── schemas/               # Pydantic models
  │     └── ticket.py
  ├── repositories/          # CRUD operations
  │     └── ticket_repository.py
  ├── services/              # Business logic
  │     └── ticket_service.py
  ├── routers/               # API endpoints
  │     └── ticket_router.py
  └── tests/                 # Unit tests
      └── test_tickets.py    # Test cases for ticket management
```

## Optional Files

- **Dockerfile**: Used to containerize the application. It defines the environment and dependencies required to run the application in a Docker container. Build the image using `docker build -t fastapi-ticket-manager .` and run it with `docker run -p 8000:8000 fastapi-ticket-manager`.

- **Makefile**: Automates common tasks such as installing dependencies, running the application, testing, linting, and building Docker images. Example commands:
  - `make install`: Install dependencies.
  - `make run`: Start the application.
  - `make test`: Run unit tests.
  - `make lint`: Check code quality with `ruff`.
  - `make build`: Build the Docker image.

- **pyproject.toml**: Configuration file for `ruff`, a fast Python linter. It specifies linting rules and settings. Run `ruff app/ tests/` to check for linting issues or `ruff app/ tests/ --fix` to auto-fix them.

## Notes
- Ensure that the `PYTHONPATH` is set correctly if running tests manually:
  ```bash
  export PYTHONPATH=$(pwd)
  ```
- Use `pytest` fixtures to reset the database state between tests.

## License
This project is licensed under the MIT License.

