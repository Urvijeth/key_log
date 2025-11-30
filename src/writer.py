import threading
from datetime import datetime
from src.config import LOG_PATH

_lock = threading.Lock()

def write_entry(text: str):
    """
    Safely append a line to the log file with a timestamp.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"{timestamp} {text}\n"

    with _lock:
        with open(LOG_PATH, "a", encoding="utf-8") as f:
            f.write(line)
            f.flush()
