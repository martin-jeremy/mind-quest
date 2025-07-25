import logging
from logging.handlers import RotatingFileHandler
import os

# logs directory
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "server.log")

# config
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        RotatingFileHandler(LOG_FILE, maxBytes=10_000_000, backupCount=3),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("mindquest")
