# gui.py
import tkinter as tk
from tkinter import messagebox
from src.logger import log_text

def on_key(event):
    """
    Called for every key pressed inside the Entry widget.
    Uses log_text() from src.logger to append to the log file.
    """
    # event.char holds printable characters; event.keysym is name for special keys
    ch = event.char if event.char else f"<{event.keysym}>"
    # Display the typed character/special key in the text area
    text_display.insert(tk.END, ch)
    text_display.see(tk.END)
    # Log the character (safe: only logs keys typed inside this app)
    try:
        log_text(ch)
    except Exception as e:
        # show a non-blocking warning if logging fails
        messagebox.showwarning("Logging Error", f"Unable to write log: {e}")

def clear_display():
    text_display.delete("1.0", tk.END)

def main():
    root = tk.Tk()
    root.title("Safe Typing Demo (In-App Only)")
    root.geometry("560x420")

    header = tk.Label(root,
                      text="Type in the box below. Keys are logged locally to logs/ (in-app only).",
                      wraplength=520,
                      justify="left")
    header.pack(pady=10, padx=8)

    entry = tk.Entry(root, width=70)
    entry.pack(pady=6)
    entry.focus_set()

    global text_display
    text_display = tk.Text(root, height=14, width=72)
    text_display.pack(pady=8)
    text_display.config(state="normal")

    # Bind only the entry widget so keys outside the app are not captured
    entry.bind("<Key>", on_key)

    btn_frame = tk.Frame(root)
    btn_frame.pack(pady=8)
    tk.Button(btn_frame, text="Clear Display", command=clear_display, width=14).grid(row=0, column=0, padx=8)
    tk.Button(btn_frame, text="Quit", command=root.destroy, width=14).grid(row=0, column=1, padx=8)

    root.mainloop()

if __name__ == "__main__":
    main()
