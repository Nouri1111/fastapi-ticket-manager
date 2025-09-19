from fastapi import FastAPI
from app.routers.ticket_router import router
from app.core.middleware import ProfilingMiddleware
from app.db.base import Base, engine
import logging
import sqlalchemy

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Add middleware
app.add_middleware(ProfilingMiddleware)

# Include routers
app.include_router(router)

def initialize_database() -> None:
    """
    Initialize the database by creating all tables.
    Logs any errors encountered during the process and verifies table creation.
    """
    try:
        logging.info("Checking registered tables in Base.metadata...")
        logging.info(f"Registered tables: {Base.metadata.tables.keys()}")
        if "tickets" not in Base.metadata.tables:
            logging.error("The 'tickets' table is not registered with Base.metadata.")
            raise RuntimeError("The 'tickets' table is missing from Base.metadata.")
        else:
            logging.info("The 'tickets' table is registered with Base.metadata.")
        
        logging.info("Creating database tables...")
        Base.metadata.create_all(bind=engine)
        logging.info("Database tables created successfully.")
        
        # Verify table creation
        with engine.connect() as connection:
            result = connection.execute(
                sqlalchemy.text("SELECT name FROM sqlite_master WHERE type='table';")
            )
            tables = [row[0] for row in result]
            logging.info(f"Existing tables in the database: {tables}")
            if "tickets" not in tables:
                logging.error("The 'tickets' table was not created in the database.")
                raise RuntimeError("The 'tickets' table is missing in the database.")
            else:
                logging.info("The 'tickets' table exists in the database.")
    except Exception as e:
        logging.error(f"Error during database initialization: {e}")
        raise

# Initialize the database
initialize_database()

@app.get("/")
def health_check():
    """
    Health check endpoint to verify the service is running.
    """
    return {"status": "ok"}