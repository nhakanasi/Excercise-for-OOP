import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

#window
window = tk.Tk()
window.title('Demo')
window.geometry('600x500')

#slider
# scale_int = tk.IntVar(value= 0)
# scale = ttk.Scale(
#     window, 
#     command= lambda value: progress.stop(),
#     from_= 0,
#     to= 25,
#     length= 300,
#     orient= "vertical",
#     variable=scale_int
#     )
# scale.pack()

# #progress bar
# progress = ttk.Progressbar(
#     window,
#     variable= scale_int,
#     maximum=25,
#     mode= 'determinate',
#     length=300,
#     )
# progress.pack()
# progress.start(1000)

# #Scrolled text
# scrolled_text = scrolledtext.ScrolledText(window)
# scrolled_text.pack()
prog_int = tk.IntVar()
progress = ttk.Progressbar(
    window,
    variable= prog_int,
    mode= 'determinate',
    length=100,
    maximum= 100,
    orient='vertical'
    )
progress.pack()
progress.start()

scale = ttk.Scale(
    window, 
    command= lambda value: progress.stop(),
    from_= 0,
    to= 100,
    orient= "vertical",
    variable=prog_int
    )
scale.pack()

text = tk.Label(textvariable=prog_int)
text.pack()

#run
window.mainloop()