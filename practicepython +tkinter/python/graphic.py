#GUI in python


import tkinter 
from tkinter  import*
t=tkinter.Tk()



#BUtton.Label,Canvas,Entry,Frame,ListBox,Menu,radiobutton,scale,spring box,scroll bar

l=Label(t,text="Enter your name",bg='red',fg='blue')


l.place(x=100,y=50)
e=Entry(t,bg='pink',fg='blue')
e.place(x=250,y=50)
t.mainloop()