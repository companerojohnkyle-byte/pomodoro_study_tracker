import tkinter as tk
from tkinter import messagebox

total_sessions = 0
timer_running = False

def countdown(seconds, label):
    global timer_running

    if seconds >= 0 and timer_running:
        mins = seconds // 60
        secs = seconds % 60
        timer_label.config(text=f"{label} Time: {mins}:{secs:02}")
        root.after(1000, countdown, seconds - 1, label)

    else:
        if timer_running:
            timer_label.config(text=f"{label} ended!")
            if label == "Study":
                messagebox.showinfo("It's Break Time", "Great job! Time for a 5-minute break!")
                countdown(5 * 60, "Break")
            else:
                timer_running = False
                timer_label.config(text="Session Complete!")

def start_session():
    global total_sessions, timer_running

    if timer_running:
        return

    try:
        minutes = entry.get()
        if minutes == "":
            minutes = 25
        else:
            minutes = int(minutes)

        total_sessions += 1
        timer_running = True
        countdown(minutes * 60, "Study")

    except ValueError:
        messagebox.showerror("Invalid Number", "Please enter a valid number.")

def show_stats():
    messagebox.showinfo("Study Stats",
                        f"Total Study Sessions Completed: {total_sessions}")

def stop_timer():
    global timer_running
    timer_running = False
    timer_label.config(text="Timer Stopped")

root = tk.Tk()
root.title("Simple Study Timer")
root.geometry("350x300")
root.resizable(False, False)

title_label = tk.Label(root, text="SIMPLE STUDY TIMER", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

entry_label = tk.Label(root, text="Enter Study Time (minutes):")
entry_label.pack()

entry = tk.Entry(root)
entry.pack(pady=5)

start_button = tk.Button(root, text="Start Study Session", command=start_session)
start_button.pack(pady=5)

stats_button = tk.Button(root, text="View Stats", command=show_stats)
stats_button.pack(pady=5)

stop_button = tk.Button(root, text="Stop Timer", command=stop_timer)
stop_button.pack(pady=5)

timer_label = tk.Label(root, text="", font=("Arial", 14))
timer_label.pack(pady=20)

root.mainloop()