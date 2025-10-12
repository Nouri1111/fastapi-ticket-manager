from sqlalchemy.orm import Session
from app.repositories.ticket_repository import (
    create_ticket, get_ticket, get_tickets, update_ticket, close_ticket
)
from app.schemas.ticket import TicketCreate, TicketUpdate
from app.models.ticket import Ticket

def create_new_ticket(db: Session, ticket_data: TicketCreate):
    """Create a new ticket."""
    new_ticket = Ticket(**ticket_data.dict())
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    return new_ticket

def get_all_tickets(db: Session) -> list[Ticket]:
    """Retrieve all tickets."""
    return get_tickets(db)

def get_ticket_by_id(db: Session, ticket_id: int) -> Ticket | None:
    """Retrieve a ticket by its ID."""
    return get_ticket(db, ticket_id)

def update_existing_ticket(db: Session, ticket_id: int, ticket_data: TicketUpdate) -> Ticket | None:
    """Update an existing ticket."""
    return update_ticket(db, ticket_id, ticket_data)

def close_existing_ticket(db: Session, ticket_id: int) -> Ticket | None:
    """Close a ticket by setting its status to 'closed'."""
    return close_ticket(db, ticket_id)