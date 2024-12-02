import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
window.title('Title')
window.geometry('600x400')

#menu
menu = tk.Menu(window)
window.configure(menu= menu)

#sub menu
file_menu = tk.Menu(menu, tearoff= False)
file_menu.add_command(label= 'New', command= lambda:print('New file'))
file_menu.add_command(label= 'Open', command= lambda:print('Open file'))
menu.add_cascade(label= 'File',menu= file_menu)

#new sub menu
help_check_string = tk.StringVar(value='on')
help_menu = tk.Menu(menu,tearoff= False)
help_menu.add_command(label= 'Help entry', command= lambda:print('AAA'))
help_menu.add_checkbutton(label= 'Check', onvalue= 'on', offvalue= 'off',variable= help_check_string)
menu.add_cascade(label= 'Help', menu= help_menu)

#More
more_menu = tk.Menu(menu,tearoff= False)
more_sub_menu = tk.Menu(more_menu, tearoff=False)
more_sub_menu.add_command(label= 'Read', command= lambda: print('Read'))
more_menu.add_cascade(label= "Read", menu= more_sub_menu)
menu.add_cascade(label= 'More', menu= more_menu)

#menu button
menu_button= ttk.Menubutton(window, text = "Menu Button")
menu_button.pack()
sub_menu= tk.Menu(menu_button, tearoff=False)
sub_menu.add_command(label='entry 1', command= lambda: print('test 1'))
sub_menu.add_checkbutton(label= 'Check', onvalue= 'on', offvalue= 'off',variable= help_check_string)
menu_button['menu']= sub_menu

#run
window.mainloop()