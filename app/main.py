from fastapi import FastAPI
from app.routers.ticket_router import router
from app.core.middleware import ProfilingMiddleware
from app.db.base import Base, engine
from app.core.logger import logger  # Use the custom logger
import sqlalchemy

app = FastAPI()

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
        logger.info("Checking registered tables in Base.metadata...")
        logger.info(f"Registered tables: {Base.metadata.tables.keys()}")
        if "tickets" not in Base.metadata.tables:
            logger.error("The 'tickets' table is not registered with Base.metadata.")
            raise RuntimeError("The 'tickets' table is missing from Base.metadata.")
        else:
            logger.info("The 'tickets' table is registered with Base.metadata.")
        
        logger.info("Creating database tables...")
        Base.metadata.create_all(bind=engine)
        logger.info("Database tables created successfully.")
        
        # Verify table creation
        with engine.connect() as connection:
            result = connection.execute(
                sqlalchemy.text("SELECT name FROM sqlite_master WHERE type='table';")
            )
            tables = [row[0] for row in result]
            logger.info(f"Existing tables in the database: {tables}")
            if "tickets" not in tables:
                logger.error("The 'tickets' table was not created in the database.")
                raise RuntimeError("The 'tickets' table is missing in the database.")
            else:
                logger.info("The 'tickets' table exists in the database.")
    except Exception as e:
        logger.error(f"Error during database initialization: {e}")
        raise

# Initialize the database
try:
    initialize_database()
except Exception as e:
    logger.critical(f"Failed to initialize the database: {e}")

@app.get("/")
def health_check():
    """
    Health check endpoint to verify the service is running.
    """
    try:
        logger.info("Health check endpoint called.")
        return {"status": "ok"}
    except Exception as e:
        logger.error(f"Error in health check endpoint: {e}")
        return {"status": "error", "detail": str(e)}