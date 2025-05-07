from pydantic import BaseModel
from typing import Literal

class RSVPCreate(BaseModel):
    response: Literal["RSVP", "Decline"]
    responder_id: str  # could be device ID or anonymous ID (optional logic)
