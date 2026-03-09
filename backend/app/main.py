from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models, database
from .routers import users, contact, appointments, habits, doctors, admin

# Create database tables
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="FreshPath API")

# Configure CORS to allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the routers
app.include_router(users.router)
app.include_router(doctors.router)
app.include_router(admin.router)
app.include_router(habits.router)
app.include_router(appointments.router)
app.include_router(contact.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to FreshPath API"}


# Serve Frontend Files
# This allows you to open index.html directly from the backend port
# current_dir = os.path.dirname(os.path.abspath(__file__))
# root_dir = os.path.abspath(os.path.join(current_dir, "../../"))
# app.mount("/", StaticFiles(directory=root_dir, html=True), name="static")
