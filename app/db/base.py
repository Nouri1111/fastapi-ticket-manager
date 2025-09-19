# app/db/base.py
from pathlib import Path
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, declarative_base

# Dossier "data" à côté de ce fichier, pour stocker app.db
DB_DIR = Path(__file__).resolve().parent / "data"
DB_DIR.mkdir(exist_ok=True)

SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_DIR / 'app.db'}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},  # requis pour SQLite dans des apps async/threads
    future=True,
    pool_pre_ping=True,
)

# Améliorations SQLite : WAL + FK ON
@event.listens_for(engine, "connect")
def set_sqlite_pragma(dbapi_connection, _):
    cur = dbapi_connection.cursor()
    cur.execute("PRAGMA journal_mode=WAL;")
    cur.execute("PRAGMA foreign_keys=ON;")
    cur.close()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)

# 1) Déclare Base AVANT d'importer les modèles
Base = declarative_base()

# 2) Importe les modèles APRÈS pour qu'ils s'enregistrent dans Base.metadata
from app.models.ticket import Ticket  # noqa: F401


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
