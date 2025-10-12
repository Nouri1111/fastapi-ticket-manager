from sqlalchemy.orm import Session
from app.models.ticket import Ticket
from app.schemas.ticket import TicketCreate, TicketUpdate
from app.core.logger import logger  # Use the custom logger

def create_ticket(db: Session, ticket: TicketCreate, location: str) -> Ticket:
    logger.info(f"Creating ticket with title: {ticket.title}, description: {ticket.description}, location: {location}")
    db_ticket = Ticket(**ticket.model_dump(), location=location)
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)
    logger.info(f"Ticket created successfully with ID: {db_ticket.id}")
    return db_ticket

def get_ticket(db: Session, ticket_id: int) -> Ticket | None:
    logger.info(f"Fetching ticket with ID: {ticket_id}")
    return db.query(Ticket).filter(Ticket.id == ticket_id).first()

def get_tickets(db: Session) -> list[Ticket]:
    logger.info("Fetching all tickets.")
    return db.query(Ticket).all()

def update_ticket(db: Session, ticket_id: int, ticket: TicketUpdate) -> Ticket:
    logger.info(f"Updating ticket with ID: {ticket_id}")
    db_ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not db_ticket:
        logger.warning(f"Ticket with ID {ticket_id} not found.")
        return None
    for key, value in ticket.model_dump(exclude_unset=True).items():  # Updated from `ticket.dict()`
        setattr(db_ticket, key, value)
    db.commit()
    db.refresh(db_ticket)
    logger.info(f"Ticket with ID {ticket_id} updated successfully.")
    return db_ticket

def close_ticket(db: Session, ticket_id: int) -> Ticket | None:
    logger.info(f"Closing ticket with ID: {ticket_id}")
    db_ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if db_ticket:
        db_ticket.status = "closed"
        db.commit()
        db.refresh(db_ticket)
        logger.info(f"Ticket with ID {ticket_id} closed successfully.")
    else:
        logger.warning(f"Ticket with ID {ticket_id} not found.")
    return db_ticket