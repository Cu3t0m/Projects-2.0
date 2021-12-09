#Libraries and components that needed importing
import tkinter as Tk
from tkinter import filedialog
from tkinter import ttk

#Start of the program
root=Tk.Tk()
l = Tk.Label(root, text="This is some sample text. Hello World!") #Text label displayed on root window
l.pack(padx=15, pady=15) #packs the label into the window

root.mainloop()