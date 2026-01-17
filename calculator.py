# My first complete Python GUI calculator
# Made by: Warid Ali



import os
import winsound

sound_path = os.path.join(os.path.dirname(__file__), "click.wav")


import tkinter as tk
import math

root = tk.Tk()
root.configure(bg="#2c2f33")

root.title("Calculator")
root.geometry("360x560")


entry = tk.Entry(root, font=("Helvetica", 30),fg="white" ,bg="black", insertbackground="white",   borderwidth=15, relief="ridge", justify="left")
entry.pack(fill="both", padx=12, pady=15)

def backspace():
     current = entry.get()
     if current:
        entry.delete(0, tk.END)
        entry.insert(tk.END, current[:-1])
        
def click(value):
    
 winsound.PlaySound(sound_path, winsound.SND_ASYNC)
    
 if value == '√':
        entry.insert(tk.END, 'sqrt(')
        
 elif value == 'x²':
        entry.insert(tk.END, '**2')
 elif value in ['sin', 'cos', 'tan', 'log']:
        entry.insert(tk.END, value + '(')
 elif value == 'C':
        clear()
 elif value == '⌫':
        backspace()
 else:
        entry.insert(tk.END, value)



def clear():
    
     winsound.PlaySound(sound_path, winsound.SND_ASYNC)
     entry.delete(0, tk.END)

    
def calculate():

    winsound.PlaySound(sound_path, winsound.SND_ASYNC)
    
    try:
        expression = entry.get()

        # 🔹 AUTO-CLOSE BRACKETS
        open_brackets = expression.count('(')
        close_brackets = expression.count(')')
        if open_brackets > close_brackets:
            expression += ')' * (open_brackets - close_brackets)

        allowed = {
            "__builtins__": None,
            "sin": lambda x: math.sin(math.radians(x)),
            "cos": lambda x: math.cos(math.radians(x)),
            "tan": lambda x: math.tan(math.radians(x)),
            "sqrt": math.sqrt,
            "log": math.log10
        }

        result = eval(expression, allowed)

        entry.delete(0, tk.END)
        entry.insert(tk.END, result)

    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def on_enter(event):
    btn = event.widget  # the button under mouse
    original_bg = btn.cget("bg")
    btn.original_bg = original_bg  # store original color
    # Change to hover color
    btn.config(bg="#5d6d7e")  # light gray for hover

def on_leave(event):
    btn = event.widget
    # Restore original color
    if hasattr(btn, "original_bg"):
        btn.config(bg=btn.original_bg)


buttons = [
    ['sin', 'cos', 'tan', '⌫'],
    ['log', '√', 'x²', 'C'],
    ['(', ')', '/', '*'],
    ['7', '8', '9', '-'],
    ['4', '5', '6', '+'],
    ['1', '2', '3', '='],
    ['0', '.', 'Clear', '']
]






frame = tk.Frame(root)
frame.pack()


for r, row in enumerate(buttons):
    for c, btn_text in enumerate(row):

        if btn_text == '':
            continue

        # 1️⃣ CREATE BUTTON
        if btn_text == 'Clear':
            btn = tk.Button(
                frame,
                text=btn_text,
                font=("Segoe UI", 20, "bold"),
                bg="#c0392b",
                fg="white",
                height=2,
                command=clear
            )
            btn.bind("<Enter>", on_enter)  # mouse enters button
            btn.bind("<Leave>", on_leave)  # mouse leaves button

        elif btn_text == '=':
            btn = tk.Button(
                frame,
                text=btn_text,
                font=("Segoe UI", 16, "bold"),
                bg="#1d8800",
                fg="white",
                width=15,
                height=2,
                command=calculate    
            )
            btn.bind("<Enter>", on_enter)  # mouse enters button
            btn.bind("<Leave>", on_leave)  # mouse leaves button

        else:
            btn = tk.Button(
                frame,
                text=btn_text,
                font=("Segoe UI", 16),
                bg="#34495e",
                fg="white",
                width=15,
                height=2,
                command=lambda b=btn_text: click(b),
            )
            btn.bind("<Enter>", on_enter)  # mouse enters button
            btn.bind("<Leave>", on_leave)  # mouse leaves button


        # 2️⃣ PLACE BUTTON (THIS IS WHERE YOUR CODE GOES)
        if btn_text == 'Clear':
            btn.grid(row=r, column=c, columnspan=2, padx=3, pady=3, sticky="nsew")
        else:
            btn.grid(row=r, column=c, padx=2, pady=2, sticky="nsew")




root.mainloop()
