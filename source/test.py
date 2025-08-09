from tkinter import *
from tkinter import ttk

def test():
    ttk.Label(frm, text="NOU                     !").grid(column=0, row=0)
    








root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="quit", command=root.destroy).grid(column=1, row=0)
ttk.Button(frm, text="change, message", command=test).grid(column=1, row=1)
root.mainloop()