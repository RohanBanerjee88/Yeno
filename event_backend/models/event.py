from fastapi import APIRouter
from uuid import uuid4
from datetime import datetime
from database.firebase import db
from schemas.event import EventCreate
from schemas.rsvp import RSVPCreate

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
    

@router.post("/event/{event_id}/rsvp")
def submit_rsvp(event_id: str, rsvp: RSVPCreate):
    try:
        # Check if event exists
        event_doc = db.collection("events").document(event_id).get()
        if not event_doc.exists:
            return {"error": "Event not found"}

        # Check for existing RSVP by responder_id
        existing = db.collection("rsvps")\
            .where("event_id", "==", event_id)\
            .where("responder_id", "==", rsvp.responder_id)\
            .get()

        if existing:
            return {"message": "You've already responded to this event."}

        # Add RSVP
        db.collection("rsvps").add({
            "event_id": event_id,
            "response": rsvp.response,
            "responder_id": rsvp.responder_id,
            "timestamp": datetime.utcnow().isoformat()
        })

        return {"message": f"Response '{rsvp.response}' recorded!"}

    except Exception as e:
        return {"error": str(e)}
    

@router.get("/event/{event_id}/summary")
def get_rsvp_summary(event_id: str):
    try:
        # Check if event exists
        event_doc = db.collection("events").document(event_id).get()
        if not event_doc.exists:
            return {"error": "Event not found"}

        # Get RSVPs
        responses = db.collection("rsvps")\
            .where("event_id", "==", event_id)\
            .stream()

        summary = []
        for r in responses:
            summary.append(r.to_dict())

        return {"responses": summary}

    except Exception as e:
        return {"error": str(e)}




