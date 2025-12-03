import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Ошибка")

window = tk.Tk()
window.title("Калькулятор")

entry = tk.Entry(window, width=30)
entry.pack(pady=10)

buttons_frame = tk.Frame(window)
buttons_frame.pack()
buttons = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    '0', 'C', '=', '/'
]

for i, text in enumerate(buttons):
    row = i // 4
    col = i % 4
    
    if text == '=':
        btn = tk.Button(buttons_frame, text=text, width=5, command=calculate)
    elif text == 'C':
        btn = tk.Button(buttons_frame, text=text, width=5, 
                       command=lambda: entry.delete(0, tk.END))
    else:
        btn = tk.Button(buttons_frame, text=text, width=5,
                       command=lambda t=text: entry.insert(tk.END, t))
    
    btn.grid(row=row, column=col, padx=2, pady=2)

window.mainloop()
