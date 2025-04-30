from fastapi import APIRouter
from uuid import uuid4
from datetime import datetime
from database.firebase import db
from schemas.event import EventCreate

router = APIRouter()

@router.post("/create-event")
def create_event(event: EventCreate):
    event_id = str(uuid4())

    event_data = {
        "uuid": event_id,
        "name": event.name,
        "location": event.location,
        "datetime": event.datetime.isoformat(),
        "payment": event.payment,
        "created_at": datetime.utcnow().isoformat(),
        "creator_id": event.creator_id
    }

    db.collection("events").document(event_id).set(event_data)

    return {"event_id": event_id, "message": "Event created successfully"}

@router.get("/event/{event_id}")
def get_event(event_id: str):
    try:
        doc = db.collection("events").document(event_id).get()
        if doc.exists:
            return doc.to_dict()
        else:
            return {"error": "Event not found"}
    except Exception as e:
        return {"error": str(e)}

