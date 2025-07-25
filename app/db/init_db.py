import logging
from app.db.session import engine
from app.db.base import Base

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def init_db():
    logger.info("Initializing database...")
    Base.metadata.create_all(bind=engine)
    logger.info("✅ Tables created sucessfully.")

if __name__ == "__main__":
    init_db()