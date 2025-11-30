# src/logger.py
"""
Safe logging functions.

This is NOT a system-wide keylogger.
It only logs:
 - Text typed in the CLI
 - Keys typed inside the GUI entry widget
"""

from src.writer import write_entry

def log_text(text: str):
    """
    Log a single character or special key from the GUI.
    """
    write_entry(text)

def log_line(line: str):
    """
    Log a full line of text from the CLI.
    """
    write_entry(line)
