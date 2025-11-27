#!/usr/bin/env python3
from src.logger import start_logger

def main():
    print("====================================")
    print("      Simple Keylogger (Safe)       ")
    print("====================================")
    print("[*] Logs will be saved inside: logs/")
    print("[*] Press CTRL + C to stop logging.")
    print("------------------------------------\n")

    start_logger()

if __name__ == "__main__":
    main()
