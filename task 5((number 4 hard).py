import tkinter as tk
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_graph():
    x = np.linspace(0, 10, 100)
    
    if var.get() == "sin":
        y = np.sin(x)
    else:
        y = np.cos(x)
    
    ax.clear()
    ax.plot(x, y)
    ax.set_title(f"График {var.get()}")
    canvas.draw()

window = tk.Tk()
window.title("График")

var = tk.StringVar(value="sin")

frame = tk.Frame(window)
frame.pack(pady=10)

tk.Radiobutton(frame, text="sin(x)", variable=var, value="sin").pack(side="left", padx=5)
tk.Radiobutton(frame, text="cos(x)", variable=var, value="cos").pack(side="left", padx=5)

tk.Button(frame, text="Построить", command=plot_graph).pack(side="left", padx=20)

figure = Figure(figsize=(5, 4))
ax = figure.add_subplot(111)

canvas = FigureCanvasTkAgg(figure, window)
canvas.get_tk_widget().pack(pady=10)

plot_graph()
window.mainloop()
