import tkinter as tk
window = tk.Tk()
window.title('Demo')
window.geometry('600x500')

#canvas
canvas = tk.Canvas(window, background= 'white')
canvas.pack()
def brush_adjustment(event):
    global brush_size
    if event.delta > 0:
        brush_size += 4
    else:
        brush_size -= 4
    brush_size = max(min(brush_size,50),0)
    
def paint (event):
    x = event.x
    y = event.y
    canvas.create_oval((x-brush_size/2, y-brush_size/2,x+ brush_size/2,y+ brush_size/2), fill= 'black')

brush_size = 2
canvas.bind('<Motion>', paint)
canvas.bind('<MouseWheel>', brush_adjustment)
#run
window.mainloop()