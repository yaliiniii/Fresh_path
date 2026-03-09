import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

# Use DATABASE_URL env var in production (Supabase), fall back to SQLite locally
SQLALCHEMY_DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "sqlite:///./freshpath.db"
)

# SQLite needs check_same_thread=False.
# PostgreSQL on Vercel serverless needs NullPool (no persistent connections between invocations).
if SQLALCHEMY_DATABASE_URL.startswith("sqlite"):
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        connect_args={"check_same_thread": False}
    )
else:
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        poolclass=NullPool  # Required for serverless: no connection pool
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

