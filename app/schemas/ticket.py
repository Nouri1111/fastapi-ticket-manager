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
    location: str  # Add the 'location' field

class TicketUpdate(TicketBase):
    status: Optional[str] = None
    location: str | None = None  # Optional 'location' field for updates

class TicketResponse(TicketBase):
    id: int
    status: str
    location: str  # Include 'location' in the response model

    model_config = ConfigDict(from_attributes=True)  # Updated from `Config`