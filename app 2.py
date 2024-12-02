import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
window.title('Title')
window.geometry('600x400')

#fucntion
def button_function():
    print('a basic button')
    print(radio_var.get())
    

#varible
button_string = tk.StringVar(value= 'a button with var')
check_var = tk.StringVar()
radio_var = tk.StringVar()

#widget
button = ttk.Button(window, text= "simple button",command= button_function,textvariable=  button_string)
button.pack()

check = ttk.Checkbutton(window, text= "check box 1", command= lambda:print(check_var.get()),variable= check_var)
check.pack()

radio1 = ttk.Radiobutton(window,text="radio but 1", value= 'radio1',variable = radio_var)
radio1.pack()
radio2 = ttk.Radiobutton(window,text="radio but 2", value= 2, variable = radio_var)
radio2.pack()

#run
window.mainloop()