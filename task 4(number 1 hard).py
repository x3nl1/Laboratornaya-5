import tkinter as tk
from tkinter import filedialog

def save_note():
    text = text_area.get("1.0", tk.END)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text)

def open_note():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
            text_area.delete("1.0", tk.END)
            text_area.insert("1.0", text)

window = tk.Tk()
window.title("Заметки")

text_area = tk.Text(window, height=20, width=50)
text_area.pack(pady=10)

button_frame = tk.Frame(window)
button_frame.pack()

save_button = tk.Button(button_frame, text="Сохранить", command=save_note)
save_button.pack(side="left", padx=5)

open_button = tk.Button(button_frame, text="Открыть", command=open_note)
open_button.pack(side="left", padx=5)

window.mainloop()
