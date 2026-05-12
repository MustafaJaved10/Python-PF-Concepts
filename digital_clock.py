# ============================================================
# PF Python - Project: Digital Clock (Tkinter GUI)
# ============================================================

import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("DIGITAL CLOCK")

label = tk.Label(
    root,
    font=('calibri', 50, 'bold'),
    background='red',
    foreground='black'
)
label.pack(anchor='center')


def update_time():
    """Fetches current time and updates the label every second."""
    string = strftime('%H:%M:%S %p \n %D')
    label.config(text=string)
    label.after(1000, update_time)   # call again after 1000ms


update_time()
root.mainloop()
