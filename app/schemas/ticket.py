from pydantic import BaseModel, ConfigDict
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

    model_config = ConfigDict(from_attributes=True)  # Updated from `Config`

class TicketCreate(TicketBase):
    pass

class TicketUpdate(TicketBase):
    status: Optional[str] = None

class TicketResponse(TicketBase):
    id: int
    status: str

    model_config = ConfigDict(from_attributes=True)  # Updated from `Config`