import tkinter as tk
from tkinter import ttk

def button_function():
    print(print(string_var.get()))
    string_var.set(value= "button pressed")

#window
window = tk.Tk()
window.title('Demo')

#varible
string_var = tk.StringVar(value= "you dumb")

#widget
label = ttk.Label(master= window, text= "label", textvariable= string_var)
label.pack()

entry = ttk.Entry(master= window,textvariable=string_var)
entry.pack()

button = ttk.Button(master= window,text= "button",command= button_function)
button.pack()

#run
window.mainloop()