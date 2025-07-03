import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

DB = "fitness.db"

# DB setup
conn = sqlite3.connect(DB)
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS entries (
    id INTEGER PRIMARY KEY,
    date TEXT,
    steps INTEGER,
    workout_mins INTEGER,
    calories INTEGER
)""")
conn.commit()
conn.close()

class FitnessApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fitness Tracker")
        self.geometry("500x600")
        self.configure(padx=20, pady=20)
        self.create_widgets()
        self.refresh_dashboard()

    def create_widgets(self):
        frame = ttk.LabelFrame(self, text="Log Activity")
        frame.pack(fill="x", pady=10)

        self.date_var = tk.StringVar(value=datetime.now().strftime("%Y-%m-%d"))
        ttk.Label(frame, text="Date (YYYY-MM-DD)").grid(row=0, column=0, sticky="w")
        ttk.Entry(frame, textvariable=self.date_var).grid(row=0, column=1)

        self.steps_var = tk.IntVar()
        ttk.Label(frame, text="Steps").grid(row=1, column=0, sticky="w")
        ttk.Entry(frame, textvariable=self.steps_var).grid(row=1, column=1)

        self.workout_var = tk.IntVar()
        ttk.Label(frame, text="Workout (mins)").grid(row=2, column=0, sticky="w")
        ttk.Entry(frame, textvariable=self.workout_var).grid(row=2, column=1)

        self.cal_var = tk.IntVar()
        ttk.Label(frame, text="Calories Burned").grid(row=3, column=0, sticky="w")
        ttk.Entry(frame, textvariable=self.cal_var).grid(row=3, column=1)

        ttk.Button(frame, text="Add / Update", command=self.save_entry).grid(row=4, column=0, columnspan=2, pady=10)

        dash_frame = ttk.LabelFrame(self, text="Dashboard")
        dash_frame.pack(fill="both", expand=True)
        self.fig, self.ax = plt.subplots(figsize=(5,3))
        self.canvas = FigureCanvasTkAgg(self.fig, master=dash_frame)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

    def save_entry(self):
        date = self.date_var.get()
        try:
            d = datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            return messagebox.showerror("Error", "Invalid date format. Use YYYY-MM-DD")

        steps = self.steps_var.get()
        workout = self.workout_var.get()
        calories = self.cal_var.get()
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute(
            "INSERT OR REPLACE INTO entries(date, steps, workout_mins, calories) VALUES (?, ?, ?, ?)",
            (date, steps, workout, calories)
        )
        conn.commit()
        conn.close()
        messagebox.showinfo("Saved", "Entry logged successfully!")
        self.refresh_dashboard()

    def refresh_dashboard(self):
        # last 7 days data
        dates = [(datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d") for i in range(6,-1,-1)]
        steps, workouts, calories = [], [], []
        conn = sqlite3.connect(DB)
        c = conn.cursor()
        for d in dates:
            c.execute("SELECT steps, workout_mins, calories FROM entries WHERE date=?", (d,))
            row = c.fetchone()
            if row:
                s,w,cal = row
            else:
                s=w=cal=0
            steps.append(s); workouts.append(w); calories.append(cal)
        conn.close()

        # Plot bar chart
        self.ax.clear()
        x = range(len(dates))
        self.ax.bar(x, steps, color='#4CAF50', label="Steps")
        self.ax.bar(x, workouts, color='#2196F3', bottom=steps, label="Workout min")
        self.ax.legend()
        self.ax.set_xticks(x); self.ax.set_xticklabels([d[5:] for d in dates])
        self.ax.set_title("Last 7 Days Activity")
        self.fig.tight_layout()
        self.canvas.draw()

if __name__ == "__main__":
    FitnessApp().mainloop()
