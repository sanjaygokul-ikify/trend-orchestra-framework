import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def configure_logging(log_file='orchestra.log'):
    handler = RotatingFileHandler(log_file, maxBytes=10000, backupCount=1)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
