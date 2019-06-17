import tkinter 
from tkinter  import*
from tkinter import messagebox
from tkinter import colorchooser

t=tkinter.Tk()
def helo():
	if messagebox.askyesno("are you sure"):
		sys.exit()
	else:
		messagebox.showinfo("thankyou")
def c():
	c=colorchooser.askcolor()
	t.config(bg=c[1])





l1=Label(t,text="New")

l1.place(x=100,y=60)
c1=Button(t,text='Submit',command=helo)
c1.place(x=100,y=100)
c2=Button(t,text='Color',command=c)
c2.place(x=100,y=150)
t.mainloop()
