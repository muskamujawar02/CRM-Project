from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

import models
import schemas
import crud

from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/frontend", StaticFiles(directory="../frontend"), name="frontend")

@app.get("/")
def home():
    return FileResponse("../frontend/index.html")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return FileResponse("frontend/index.html")


@app.post("/api/tickets")
def create_ticket(
    ticket: schemas.TicketCreate,
    db: Session = Depends(get_db)
):
    new_ticket = crud.create_ticket(db, ticket)

    return {
        "ticket_id": new_ticket.ticket_id,
        "created_at": new_ticket.created_at
    }

@app.get("/api/tickets")
def get_tickets(
    search: str = None,
    status: str = None,
    db: Session = Depends(get_db)
):
    tickets = crud.get_all_tickets(
        db,
        search,
        status
    )

    return tickets

@app.get("/api/tickets/{ticket_id}")
def get_ticket(
    ticket_id: str,
    db: Session = Depends(get_db)
):
    ticket = crud.get_ticket(db, ticket_id)

    if not ticket:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    return ticket

@app.put("/api/tickets/{ticket_id}")
def update_ticket(
    ticket_id: str,
    ticket: schemas.TicketUpdate,
    db: Session = Depends(get_db)
):

    updated_ticket = crud.update_ticket(
        db,
        ticket_id,
        ticket.status,
        ticket.notes
    )

    if not updated_ticket:
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )

    return {
        "success": True,
        "updated_at": updated_ticket.updated_at
    }