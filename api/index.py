import sys
import os

# Ensure project root is importable
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app import models, database
from backend.app.routers import users, contact, appointments, habits, doctors, admin

# Create tables on first deploy (safe to call multiple times)
try:
    models.Base.metadata.create_all(bind=database.engine)
except Exception as e:
    print(f"Warning: Could not auto-create tables: {e}")

app = FastAPI(title="FreshPath API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include every router under /api so Vercel's rewrite (/api/* → this file)
# works without any path stripping — FastAPI routes become /api/users/signup etc.
app.include_router(users.router, prefix="/api")
app.include_router(doctors.router, prefix="/api")
app.include_router(admin.router, prefix="/api")
app.include_router(habits.router, prefix="/api")
app.include_router(appointments.router, prefix="/api")
app.include_router(contact.router, prefix="/api")


@app.get("/api")
def api_root():
    return {"message": "Welcome to FreshPath API"}
