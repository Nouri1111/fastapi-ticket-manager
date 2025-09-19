import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.db.base import get_db, Base, engine
from sqlalchemy.orm import sessionmaker

# Setup test database
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture(autouse=True)
def clear_database():
    """
    Clear the database before each test to ensure a clean state.
    """
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

# Test health check
def test_health_check():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

# Test creating a ticket
def test_create_ticket():
    response = client.post("/tickets/", json={"title": "Test Ticket", "description": "Test Description"})
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Ticket"
    assert data["description"] == "Test Description"
    assert data["status"] == "open"

# Test creating a ticket with missing fields
def test_create_ticket_missing_fields():
    response = client.post("/tickets/", json={})
    assert response.status_code == 422

# Test listing tickets
def test_list_tickets():
    client.post("/tickets/", json={"title": "Ticket 1", "description": "Description 1"})
    client.post("/tickets/", json={"title": "Ticket 2", "description": "Description 2"})
    response = client.get("/tickets/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2  # Ensure only the two tickets created in this test are returned

# Test retrieving a ticket
def test_get_ticket():
    response = client.post("/tickets/", json={"title": "Ticket", "description": "Description"})
    ticket_id = response.json()["id"]
    response = client.get(f"/tickets/{ticket_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == ticket_id

# Test retrieving a non-existent ticket
def test_get_non_existent_ticket():
    response = client.get("/tickets/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Ticket not found"

# Test updating a ticket
def test_update_ticket():
    response = client.post("/tickets/", json={"title": "Old Title", "description": "Old Description"})
    ticket_id = response.json()["id"]
    response = client.put(f"/tickets/{ticket_id}", json={"title": "New Title", "description": "New Description", "status": "stalled"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "New Title"
    assert data["description"] == "New Description"
    assert data["status"] == "stalled"

# Test updating a non-existent ticket
def test_update_non_existent_ticket():
    response = client.put("/tickets/999", json={"title": "Title", "description": "Description", "status": "open"})
    assert response.status_code == 404
    assert response.json()["detail"] == "Ticket not found"

# Test closing a ticket
def test_close_ticket():
    response = client.post("/tickets/", json={"title": "Ticket", "description": "Description"})
    ticket_id = response.json()["id"]
    response = client.patch(f"/tickets/{ticket_id}/close")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "closed"

# Test closing a non-existent ticket
def test_close_non_existent_ticket():
    response = client.patch("/tickets/999/close")
    assert response.status_code == 404
    assert response.json()["detail"] == "Ticket not found"

# Move test cases to match the application's structure
# For example, tests related to routers should go into `tests/app/routers/`.
# Similarly, tests for services, repositories, etc., should be placed in their respective directories.

# This file will now serve as an entry point or integration test file if needed.