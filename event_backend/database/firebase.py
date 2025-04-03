import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore

# Load environment variables from .env file
load_dotenv()

# Get key path from environment
key_path = os.getenv("FIREBASE_KEY_PATH")

# Initialize Firebase app
cred = credentials.Certificate(key_path)
firebase_admin.initialize_app(cred)

# Create Firestore client
db = firestore.client()
