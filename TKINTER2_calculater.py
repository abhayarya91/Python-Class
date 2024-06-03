import tkinter as tk

root = tk.Tk()
root.title("Calculator")

menubar = tk.Menu(root)
root.config(menu=menubar)

edit_menu = tk.Menu(menubar)
menubar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=lambda: print("Cut option clicked"))
edit_menu.add_command(label="Copy", command=lambda: print("Copy option clicked"))
edit_menu.add_command(label="Paste", command=lambda: print("Paste option clicked"))

view_menu = tk.Menu(menubar)
menubar.add_cascade(label="View", menu=view_menu)
view_menu.add_command(label="Standard", command=lambda: print("Standard view option clicked"))
view_menu.add_command(label="Scientific", command=lambda: print("Scientific view option clicked"))

help_menu = tk.Menu(menubar)
menubar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=lambda: print("About option clicked"))

display = tk.Entry(root, width=25, font=('Arial', 16), bd=10, insertwidth=2, bg="black", justify='right')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

f_num = None
math = ""

def button_click(number):
    current_text = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current_text + str(number))

def button_operation(operator):
    global f_num, math
    f_num = display.get()
    math = operator
    display.delete(0, tk.END)
    display.insert(tk.END, f_num + operator)

def button_clear():
    global f_num, math
    display.delete(0, tk.END)
    f_num = None
    math = ""

def button_equal():
    global f_num, math
    second_number = display.get()[len(f_num) + 1:]
    display.delete(0, tk.END)
    try:
        if math == "+":
            result = float(f_num) + float(second_number)
        elif math == "-":
            result = float(f_num) - float(second_number)
        elif math == "*":
            result = float(f_num) * float(second_number)
        elif math == "/":
            if float(second_number) == 0:
                result = "Error: Div by 0"
            else:
                result = float(f_num) / float(second_number)
        display.insert(0, str(result))
    except:
        display.insert(0, "Error")
    f_num = None
    math = ""

button_1 = tk.Button(root, text="1", padx=20, pady=20, font=('Arial', 18), bg="light grey", fg="black", command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx=20, pady=20, font=('Arial', 18), bg="light grey", fg="black", command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", padx=20, pady=20, font=('Arial', 18), bg="light grey", fg="black", command=lambda: button_click(3))
button_4 = tk.Button(root, text="4", padx=20, pady=20, font=('Arial', 18), bg="light grey", fg="black", command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", padx=20, pady=20, font=('Arial', 18), bg="light grey", fg="black", command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", padx=20, pady=20, font=('Arial', 18), bg="light grey", fg="black", command=lambda: button_click(6))
button_7 = tk.Button(root, text="7", padx=20, pady=20, font=('Arial', 18), bg="light grey", fg="black", command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", padx=20, pady=20, font=('Arial', 18), bg="light grey", fg="black", command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", padx=20, pady=20, font=('Arial', 18), bg="light grey", fg="black", command=lambda: button_click(9))
button_0 = tk.Button(root, text="0", padx=20, pady=20, font=('Arial', 18), bg="light grey", fg="black", command=lambda: button_click(0))

button_add = tk.Button(root, text="+", padx=19, pady=20, font=('Arial', 18), bg="orange", fg="black", command=lambda: button_operation("+"))
button_equal = tk.Button(root, text="=", padx=47, pady=20, font=('Arial', 18), bg="green", fg="black", command=button_equal)
button_clear = tk.Button(root, text="Clear", padx=35, pady=20, font=('Arial', 18), bg="red", fg="black", command=button_clear)
button_subtract = tk.Button(root, text="-", padx=21, pady=20, font=('Arial', 18), bg="orange", fg="black", command=lambda: button_operation("-"))
button_multiply = tk.Button(root, text="*", padx=20, pady=20, font=('Arial', 18), bg="orange", fg="black", command=lambda: button_operation("*"))
button_divide = tk.Button(root, text="/", padx=21, pady=20, font=('Arial', 18), bg="orange", fg="black", command=lambda: button_operation("/"))

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_divide.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_multiply.grid(row=2, column=3)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_subtract.grid(row=3, column=3)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_equal.grid(row=4, column=2, columnspan=2)
button_add.grid(row=5, column=0, columnspan=4)

root.mainloop()
