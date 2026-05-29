from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class TicketCreate(BaseModel):
    customer_name: str
    customer_email: EmailStr
    subject: str
    description: str

class TicketUpdate(BaseModel):
    status: str
    notes: Optional[str] = ""

class TicketResponse(BaseModel):
    ticket_id: str
    customer_name: str
    customer_email: str
    subject: str
    description: str
    status: str
    notes: str
    created_at: datetime

    class Config:
        orm_mode = True