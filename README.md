# Safe Key Logging Demo (Educational & In-App Only)

This project demonstrates a **safe and ethical key-logging concept** for cybersecurity learning and internship tasks.  
It does **NOT** record system-wide keystrokes.  
It only logs typing done **inside the CLI** 
---

##  Project Structure

key_log/  
├── main.py  
├── gui.py  
├── README.md  
│  
├── src/  
│   ├── __init__.py  
│   ├── config.py  
│   ├── logger.py  
│   └── writer.py  
│  
└── logs/  

---

##  Requirements

- Python 3.8 or above  
- Tkinter (installed by default on Windows/Linux, install manually if needed)

Ubuntu/Debian install:
sudo apt install python3-tk

---

##  How to Run the Project

### 1️ CLI Mode (Default)
Use this command:
python main.py

How it works:
- Type anything → the text is logged  
- Press Enter on an empty line → program exits  

---

##  Where Logs Are Saved

Logs are created automatically in:
key_log/logs/

Each run creates a new file:
safe_keys_YYYYMMDD_HHMMSS.txt

Example:
safe_keys_20250301_143012.txt

To view a log:
cat logs/<filename>

---


##  Quick Command Summary

Run CLI:
python main.py

Run GUI:
python main.py --mode gui

View logs:
ls logs
cat logs/<filename>

---