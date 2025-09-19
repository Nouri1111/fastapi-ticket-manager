# FastAPI Ticket Manager

## Overview
This project is a FastAPI-based backend application for managing tickets. It includes features such as creating, updating, listing, and closing tickets. The application follows a clean, layered architecture and uses SQLite as an in-memory database.

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

## Requirements
- Python 3.10+
- FastAPI
- Uvicorn
- SQLite (in-memory)

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
pytest --cov=app tests/
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
      └── ...
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
