from tkinter import *
from tkinter.ttk import *
from time import strftime 

root = Tk()
root.title("Menu Demonstration")

menubar = Menu(root)

file = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=file)
file.add_command(label='New File', command=None)
file.add_command(label='Open...', command=None)
file.add_command(label='Save...', command=None)
file.add_separator()
file.add_command(label='Exit', command=root.destroy)

help_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='Help 1', command=None)
help_menu.add_command(label='Help 2', command=None)
help_menu.add_command(label='Help 3', command=None)

edit_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Edit File 1', command=None)
edit_menu.add_command(label='Edit File 2', command=None)
edit_menu.add_command(label='Edit File 3', command=None)

root.config(menu=menubar) 
root.mainloop()


