import tkinter as tk
from tkinter import messagebox

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

class CalculatorGUI:
    def __init__(self, root):
        self.calc = Calculator()
        self.root = root
        self.root.title("Calculator")

        self.entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid")
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', 'x',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button_text in buttons:
            button = tk.Button(root, text=button_text, font=('Arial', 18), width=4, height=2)
            button.grid(row=row_val, column=col_val)
            button.bind("<Button-1>", self.on_button_click)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        clear_button = tk.Button(root, text='C', font=('Arial', 18), width=4, height=2)
        clear_button.grid(row=row_val, column=col_val)
        clear_button.bind("<Button-1>", self.on_button_click)

    def on_button_click(self, event):
        key = event.widget.cget("text")
        if key == '=':
            try:
                expression = self.entry.get().replace('x', '*')
                result = eval(expression)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
        elif key == 'C':
            self.entry.delete(0, tk.END)
        else:
            self.entry.insert(tk.END, key)

if __name__ == "__main__":
    root = tk.Tk()
    gui = CalculatorGUI(root)
    root.mainloop()