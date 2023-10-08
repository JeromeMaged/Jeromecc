import tkinter as tk
from tkinter import ttk

def display_info():
    selected_item = combo.get()
    info_text.delete(1.0, tk.END)  # Clear the text area
    if selected_item == "How do eclipses occur?":
        info_text.insert(tk.END, "Eclipses occur when the Moon passes between the Earth and the Sun.")
    elif selected_item == "Why do only some people see an eclipse?":
        info_text.insert(tk.END, "Eclipses are only visible in the region covered by the Moon's shadow.")
    # Add more explanations for other questions

app = tk.Tk()
app.title("Eclipse Explorer")

frame = ttk.Frame(app)
frame.grid(row=0, column=0, padx=10, pady=10)

label = ttk.Label(frame, text="Select a question:")
label.grid(row=0, column=0, padx=5, pady=5)

combo = ttk.Combobox(frame, values=[
    "How do eclipses occur?",
    "Why do only some people see an eclipse?",
    "What causes the Sun, Moon, and Earth to align?",
    "How often do eclipses occur?",
    "How do scientists predict eclipses?",
    "What is the difference between lunar and solar eclipses?",
    "What is an eclipse season and why do they occur approximately every six months?"
])
combo.grid(row=0, column=1, padx=5, pady=5)

display_button = ttk.Button(frame, text="Display Info", command=display_info)
display_button.grid(row=0, column=2, padx=5, pady=5)

info_text = tk.Text(frame, height=5, width=50)
info_text.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

app.mainloop()
