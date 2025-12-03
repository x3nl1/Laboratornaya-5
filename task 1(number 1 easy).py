import tkinter as tk

window = tk.Tk()
window.title("Привет")

label = tk.Label(window, text="Нажми кнопку")
label.pack(pady=20)

button = tk.Button(window, text="Привет", 
command=lambda: label.config(text="Привет, мир!"))
button.pack(pady=10)

window.mainloop()
