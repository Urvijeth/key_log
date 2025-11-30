#!/usr/bin/env python3

import argparse
from src.logger import log_line

def run_cli():
    print("======================================")
    print("       SAFE KEY LOGGING (CLI)         ")
    print("======================================")
    print("Type anything and press Enter to log.")
    print("Leave the line EMPTY and press Enter to exit.")
    print("--------------------------------------")

    while True:
        try:
            line = input("> ")
        except (KeyboardInterrupt, EOFError):
            print("\n[!] Exiting CLI logger.")
            break

        if line.strip() == "":
            print("[*] Empty line entered → exiting.")
            break

        log_line(line)
        print("[+] Logged.")

def main():
    parser = argparse.ArgumentParser(description="Safe Key Logging Demo")
    parser.add_argument(
        "--mode",
        choices=["cli", "gui"],
        default="cli",
        help="Choose CLI or GUI mode"
    )

    args = parser.parse_args()

    if args.mode == "gui":
        import gui  # import GUI only when needed
        gui.main()
    else:
        run_cli()

if __name__ == "__main__":
    main()
