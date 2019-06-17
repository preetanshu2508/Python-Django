import tkinter
from tkinter import*

t=tkinter.Tk()
x=IntVar()
def f():
	g=x.get()
	if g==1:
		t.config(bg='red')
	elif g==2:
		t.config(bg='green')
	elif g==3:
	    t.config(bg='yellow')
r1=Radiobutton(t,text="Red",intvariable=x,value=1)
r2=Radiobutton(t,text="Red",intvariable=x,value=2)
r3=Radiobutton(t,text="Red",intvariable=x,value=3)
r1.place(x=100,y=100)
r2.place(x=100,y=150)
r3.place(x=100,y=200)
e=Button(t,text='Apply',command=f)

e.place(x=100,y=280)
t.mainloop()

