# src/config.py
import os
from datetime import datetime

# Project root directory (folder containing your project)
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Logs folder path
LOG_DIR = os.path.join(ROOT_DIR, "logs")

# Ensure logs folder exists
os.makedirs(LOG_DIR, exist_ok=True)

# Create a new log filename with timestamp
LOG_FILENAME = f"safe_keys_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

# Full path to log file
LOG_PATH = os.path.join(LOG_DIR, LOG_FILENAME)
