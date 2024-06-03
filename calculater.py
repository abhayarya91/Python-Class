import tkinter as tk

gui = tk.Tk()
gui.configure(background="blue")
gui.title("Simple Calculator")
gui.geometry("217x300")  # Corrected the geometry string

menu = tk.Menu(gui)
gui.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New")
file_menu.add_separator()
file_menu.add_command(label="Exit")

edit_menu = tk.Menu(menu)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Add")

help_menu = tk.Menu(menu)
menu.add_cascade(label="Help", menu=help_menu)

entry_field = tk.Entry(gui)
entry_field.pack()

def button_click(value):
    entry_field.insert(tk.END, value)

for i in range(10):
    button_digit = tk.Button(gui, text=str(i), command=lambda i=i: button_click(str(i)))
    button_digit.pack(side=tk.LEFT, padx=5, pady=5)

button_add = tk.Button(gui, text="+", command=lambda: button_click("+"))
button_add.pack(side=tk.LEFT, padx=5, pady=5)

button_subtract = tk.Button(gui, text="-", command=lambda: button_click("-"))
button_subtract.pack(side=tk.LEFT, padx=5, pady=5)

button_multiply = tk.Button(gui, text="*", command=lambda: button_click("*"))
button_multiply.pack(side=tk.LEFT, padx=5, pady=5)

button_divide = tk.Button(gui, text="/", command=lambda: button_click("/"))
button_divide.pack(side=tk.LEFT, padx=5, pady=5)

gui.mainloop()
