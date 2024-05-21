from fastapi import FastAPI

app = FastAPI()

from fastapi import HTTPException
from models import Event
from schemas import EventCreate  # Assuming I have defined Pydantic schemas for event creation

@app.post("/events/")
async def create_event(event: EventCreate):
    # Add logic to insert a new event into the database
    return {"event_name": event.name, "location": event.location}