import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
window.title('Layout')
window.geometry('600x400')

#pack (chen cho du cho), grid (phan o), place (dat vao vi tri)
label1 = ttk.Label(window,text= 'Label 1', background= 'red')
label2 = ttk.Label(window,text= 'Label 2', background= 'blue')

#pack
# label1.pack(side='left', expand= True, fill="both")
# label2.pack(side= 'bottom')
label1.pack(side='top',expand= True)

#run
window.mainloop()