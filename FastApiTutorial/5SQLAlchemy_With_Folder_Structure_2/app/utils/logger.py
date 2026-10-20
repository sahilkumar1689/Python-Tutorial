import logging
from logging.handlers import RotatingFileHandler
import os

# Create logs directory
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# --- File paths ---
INFO_LOG_FILE = os.path.join(LOG_DIR, "info.log")
ERROR_LOG_FILE = os.path.join(LOG_DIR, "error.log")

# --- Formatters ---
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

# --- Handlers ---
# Info handler (INFO and above, but exclude ERROR)
info_handler = RotatingFileHandler(
    INFO_LOG_FILE, maxBytes=5*1024*1024, backupCount=5, encoding="utf-8"
)
info_handler.setLevel(logging.INFO)
info_handler.setFormatter(formatter)

# Error handler (only ERROR and CRITICAL)
error_handler = RotatingFileHandler(
    ERROR_LOG_FILE, maxBytes=5*1024*1024, backupCount=5, encoding="utf-8"
)
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(formatter)

# Console handler (for development)
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# --- Logger setup ---
logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)  # capture everything, handlers filter by level
logger.addHandler(info_handler)
logger.addHandler(error_handler)
logger.addHandler(console_handler)
