# app/models/ticket.py
from sqlalchemy import Column, Integer, String, Text, DateTime, func
from app.db.base import Base

class Ticket(Base):
    __tablename__ = "tickets"  # Must match exactly with the database table name

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    status = Column(String(50), default="open", index=True)
    created_at = Column(DateTime, server_default=func.now())
