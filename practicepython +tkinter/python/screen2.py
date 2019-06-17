import tkinter 
from tkinter  import*
t=tkinter.Tk()

#to make menu
mb=Menu(t)
f=Menu(mb)
mb.add_cascade(label="File",menu=f)
f.add_command(label="New")
f.add_separator()
f.add_command(label="Save As")
f.add_separator()
f.add_command(label="Save")
f.add_separator()
f.add_command(label="Open Folder")
f.add_separator()
f.add_command(label="Close Window")
f.add_separator()

t.config(menu=mb)



e=Menu(mb)
mb.add_cascade(label="Edit",menu=e)

e.add_command(label="New")
e.add_separator()
e.add_command(label="Save As")
e.add_separator()
e.add_command(label="Save")




t.mainloop()

#


