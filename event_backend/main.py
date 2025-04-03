from fastapi import FastAPI
from database.firebase import db  # Firestore client

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Event Card API is running 🚀"}

@app.get("/test-db")
def test_db_connection():
    try:
        # Try writing a test document
        doc_ref = db.collection("test").document("connection-test")
        doc_ref.set({"status": "connected"})

        # Try reading it back
        doc = doc_ref.get()
        return {"status": doc.to_dict()["status"]}
    except Exception as e:
        return {"error": str(e)}
