import os
from fastapi import FastAPI
from sqlalchemy import text, create_engine

app = FastAPI(title="FastAPI + Postgres + Compose")

database_url = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://postgres:postgres@db:5432/fastapi_db"
)
engine = create_engine(database_url, pool_pre_ping=True)

@app.get("/health")
def health():
    with engine.connect() as conn:
        ok = conn.execute(text("SELECT 1")).scalar()
    return {"status": "ok", "db": ok}

@app.get("/")
def root():
    return {"message": "FastAPI is up. Use pgAdmin at http://localhost:5050"}
