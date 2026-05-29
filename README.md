# Customer Support Ticketing CRM System

A full-stack Customer Support CRM System built using FastAPI, SQLite, HTML, CSS, and JavaScript.

## Features

- Create support tickets
- View all tickets
- Search tickets
- Filter tickets by status
- View ticket details
- Update ticket status
- Add notes/comments

## Tech Stack

### Backend
- FastAPI
- SQLite
- SQLAlchemy

### Frontend
- HTML
- CSS
- JavaScript

## Project Structure

crm_project/
│
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── detail.html
│   ├── style.css
│   └── app.js

## API Endpoints

POST /api/tickets

GET /api/tickets

GET /api/tickets/{ticket_id}

PUT /api/tickets/{ticket_id}

## How to Run Backend

cd backend

uvicorn main:app --reload

## How to Run Frontend

Open index.html using Live Server extension in VS Code.

## Author

Muskan Mujawar