import tkinter as tk
def press(num):
    entry_text.set(entry_text.get() + str(num))
    
def equal():
    try:
        result = str(eval(entry_text.get()))
        entry_text.set(result)
    except ZeroDivisionError:
        entry_text.set("Error: Division by 0")
    except Exception:
        entry_text.set("Error")

def clear():
    entry_text.set("")

app = tk.Tk()
app.title("Simple Calculator")
app.geometry("300x400")
app.resizable(False, False)

entry_text = tk.StringVar()
entry = tk.Entry(app, textvariable=entry_text, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4, relief='ridge', justify="right")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

for (text, row, col) in buttons:
    action = lambda x=text: press(x) if x not in ['=', 'C'] else equal() if x == '=' else clear()
    tk.Button(app, text=text, padx=20, pady=20, font=("Arial", 12), command=action).grid(row=row, column=col, sticky="nsew")

for i in range(6):
    app.grid_rowconfigure(i, weight=1)
for i in range(4):
    app.grid_columnconfigure(i, weight=1)

app.mainloop()
