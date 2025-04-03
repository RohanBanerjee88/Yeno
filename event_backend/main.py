from fastapi import FastAPI
from routers import events, rsvp

app = FastAPI()

# Include route modules
# app.include_router(events.router)
# app.include_router(rsvp.router)

@app.get("/")
def root():
    return {"message": "Event Card API is running 🚀"}
