import tkinter
from tkinter import messagebox
top = tkinter.Tk()
def fun():
    messagebox.showinfo("click me.....","Hello bhai....band kr ise aage ki padhai kr:")
b = tkinter.Button(top,text= "say Hello",command= fun).pack()
b = tkinter.Button(top,text="Exit",command=top.destroy).pack()
top.mainloop()