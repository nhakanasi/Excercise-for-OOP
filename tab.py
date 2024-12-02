import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
window.title('Title')
window.geometry('600x400')

#notebook widget
notebook = ttk.Notebook(window)

#tab1
tab1 = ttk.Frame(notebook)
label1 = ttk.Label(tab1, text= 'Text in 1')
label1.pack()
button1 = ttk.Button(tab1, text= 'button in 1')
button1.pack()

#tab2
tab2 = ttk.Frame(notebook)
label2 = ttk.Label(tab2,text= 'text in 2')
label2.pack()
entry2 = ttk.Entry(tab2)
entry2.pack()

notebook.add(tab1,text= 'tab1')
notebook.add(tab2,text= 'tab2')
notebook.pack()

#run
window.mainloop()