from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.base import get_db
from app.schemas.ticket import TicketCreate, TicketUpdate, TicketResponse
from app.services.ticket_service import (
    create_new_ticket, get_all_tickets, get_ticket_by_id,
    update_existing_ticket, close_existing_ticket
)
from app.core.logger import logger  # Ensure logger is used for error logging

router = APIRouter(prefix="/tickets", tags=["Tickets"])

# Ajout d'un champ 'location' dans les endpoints concernés
@router.post("/", response_model=TicketResponse, status_code=status.HTTP_201_CREATED)
def create_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    try:
        logger.info("Creating a new ticket.")
        return create_new_ticket(db, ticket, ticket.location)  # Ensure location is passed from TicketCreate
    except Exception as e:
        logger.error(f"Error creating ticket: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")

@router.get("/", response_model=list[TicketResponse])
def list_tickets(db: Session = Depends(get_db)):
    try:
        logger.info("Fetching all tickets.")
        return get_all_tickets(db)
    except Exception as e:
        logger.error(f"Error fetching tickets: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")

@router.get("/{ticket_id}", response_model=TicketResponse)
def get_ticket(ticket_id: int, db: Session = Depends(get_db)):
    try:
        logger.info(f"Fetching ticket with ID: {ticket_id}")
        ticket = get_ticket_by_id(db, ticket_id)
        if not ticket:
            logger.warning(f"Ticket with ID {ticket_id} not found.")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ticket not found")
        return ticket
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Error fetching ticket with ID {ticket_id}: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")

@router.put("/{ticket_id}", response_model=TicketResponse)
def update_ticket(ticket_id: int, ticket: TicketUpdate, db: Session = Depends(get_db)):
    try:
        logger.info(f"Updating ticket with ID: {ticket_id}")
        updated_ticket = update_existing_ticket(db, ticket_id, ticket)
        if not updated_ticket:
            logger.warning(f"Ticket with ID {ticket_id} not found.")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ticket not found")
        return updated_ticket
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Error updating ticket with ID {ticket_id}: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")

@router.patch("/{ticket_id}/close", response_model=TicketResponse)
def close_ticket(ticket_id: int, db: Session = Depends(get_db)):
    try:
        logger.info(f"Closing ticket with ID: {ticket_id}")
        closed_ticket = close_existing_ticket(db, ticket_id)
        if not closed_ticket:
            logger.warning(f"Ticket with ID {ticket_id} not found.")
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Ticket not found")
        return closed_ticket
    except HTTPException as e:
        raise e
    except Exception as e:
        logger.error(f"Error closing ticket with ID {ticket_id}: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")