from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class TicketStatus(str, Enum):
    OPEN = "open"
    STALLED = "stalled"
    CLOSED = "closed"

class TicketBase(BaseModel):
    title: str
    description: str | None = None
    status: TicketStatus = TicketStatus.OPEN

class TicketCreate(TicketBase):
    pass

class TicketUpdate(TicketBase):
    pass

class TicketResponse(TicketBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True