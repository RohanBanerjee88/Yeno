from fastapi import FastAPI
from database.firebase import db
from models import event

app = FastAPI()
app.include_router(event.router)

@app.get("/")
def root():
    return {"message": "Event Card API is running 🚀"}

@app.get("/test-db")
def test_db_connection():
    try:
        doc_ref = db.collection("test").document("connection-test")
        doc_ref.set({"status": "connected"})
        doc = doc_ref.get()
        return {"status": doc.to_dict()["status"]}
    except Exception as e:
        return {"error": str(e)}
