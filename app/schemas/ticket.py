from pydantic import BaseModel
from datetime import datetime
from enum import Enum
from typing import Optional

class TicketStatus(str, Enum):
    OPEN = "open"
    STALLED = "stalled"
    CLOSED = "closed"

class TicketBase(BaseModel):
    title: str
    description: Optional[str] = None

    class Config:
        from_attributes = True  # Updated from `orm_mode = True`

class TicketCreate(TicketBase):
    pass

class TicketUpdate(TicketBase):
    status: Optional[str] = None

class TicketResponse(TicketBase):
    id: int
    status: str

    class Config:
        from_attributes = True  # Updated from `orm_mode = True`