import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
window.geometry('600x400+0+0') #length x height + x_pos + y_pos
window.iconbitmap('python.ico')

#window sizes
window.minsize(200,100)

#screen
print(window.winfo_screenwidth())
print(window.winfo_screenheight())

#window attributes
window.attributes('-alpha',1 )
# window.attributes('-topmost',True)
# window.attributes('-fullscreen',True)
window.title('Style')
window.overrideredirect(True)
grip = ttk.Sizegrip(window)
grip.place(relx=1.0,rely=1.0,anchor='se')

#security event
window.bind('<Escape>',lambda event: window.quit())

#run
window.mainloop()