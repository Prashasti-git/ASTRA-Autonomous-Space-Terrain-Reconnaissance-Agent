import os
from fastapi import FastAPI
from sqlalchemy import create_engine, text

app = FastAPI(
    title="ASTRA Autonomous Rover Backend API",
    version="1.0.0",
    description="Backend API and Telemetry Service for ASTRA Rover"
)

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/astra_db")


def check_database_connection() -> str:
    """Checks database connectivity using DATABASE_URL."""
    if not DATABASE_URL:
        return "not_configured"

    # Convert asyncpg scheme if passed for sync engine check or use standard sync driver
    db_url = DATABASE_URL
    if db_url.startswith("postgresql+asyncpg://"):
        db_url = db_url.replace("postgresql+asyncpg://", "postgresql://", 1)

    try:
        engine = create_engine(db_url, connect_args={"connect_timeout": 2})
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return "connected"
    except Exception:
        return "disconnected"


@app.get("/")
def get_root():
    return {"system": "ASTRA", "status": "online"}


@app.get("/health")
def get_health():
    db_status = check_database_connection()
    return {
        "backend": "healthy",
        "database": db_status
    }
