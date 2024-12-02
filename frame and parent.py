import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
window.title('Demo')
window.geometry('600x400')

#frame
frame = ttk.Frame(window,width= 200,height=200,borderwidth=10,relief= tk.GROOVE)
frame.pack_propagate(False)
frame.pack()

#master setting
label = ttk.Label(frame, text = 'Label in frame')
label.pack()

button = ttk.Button(frame, text = 'Button in a frame')
button.pack()

label2 = ttk.Label(window, text = "outSide the frame")
label2.pack()

#run
window.mainloop()