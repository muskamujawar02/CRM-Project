from sqlalchemy.orm import Session
from models import Ticket
from datetime import datetime
import random

def generate_ticket_id():
    number = random.randint(1000, 9999)
    return f"TKT-{number}"

def create_ticket(db: Session, ticket):
    new_ticket = Ticket(
        ticket_id=generate_ticket_id(),
        customer_name=ticket.customer_name,
        customer_email=ticket.customer_email,
        subject=ticket.subject,
        description=ticket.description,
        status="Open"
    )

    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)

    return new_ticket

def get_all_tickets(db: Session, search=None, status=None):

    query = db.query(Ticket)

    if search:
        query = query.filter(
            Ticket.customer_name.contains(search) |
            Ticket.customer_email.contains(search) |
            Ticket.subject.contains(search) |
            Ticket.description.contains(search) |
            Ticket.ticket_id.contains(search)
        )

    if status:
        query = query.filter(Ticket.status == status)

    return query.all()

def get_ticket(db: Session, ticket_id: str):
    return db.query(Ticket).filter(
        Ticket.ticket_id == ticket_id
    ).first()

def update_ticket(db: Session, ticket_id: str, status: str, notes: str):

    ticket = db.query(Ticket).filter(
        Ticket.ticket_id == ticket_id
    ).first()

    if ticket:
        ticket.status = status
        ticket.notes = notes
        ticket.updated_at = datetime.utcnow()

        db.commit()
        db.refresh(ticket)

    return ticket