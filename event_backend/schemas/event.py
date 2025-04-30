from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class EventCreate(BaseModel):
    name: str
    location: str
    datetime: datetime
    payment: Optional[float] = None
    creator_id: Optional[str] = None 
