import logging
from logging.handlers import RotatingFileHandler
import os
from datetime import datetime

try:
    # Ensure the log directory exists at the root of the project
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))  # Root directory
    LOG_DIR = os.path.join(BASE_DIR, "log")
    os.makedirs(LOG_DIR, exist_ok=True)

    # Generate log filename based on the current date
    LOG_FILE = os.path.join(LOG_DIR, f"fastapi-ticket-manager_{datetime.now().strftime('%Y-%m-%d')}.log")

    # Configure the logger
    logger = logging.getLogger("fastapi-ticket-manager")
    logger.setLevel(logging.INFO)

    # Rotating file handler: keeps the last 3 log files, each up to 1MB
    file_handler = RotatingFileHandler(LOG_FILE, maxBytes=1_000_000, backupCount=3)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Stream handler for console output
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

except Exception as e:
    print(f"Failed to configure logging: {e}")
    raise
