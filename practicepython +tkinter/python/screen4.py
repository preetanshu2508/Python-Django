import tkinter
from tkinter import*
from tkinter import messagebox
t=tkinter.Tk()
s=IntVar()
w=IntVar()
def Cal():
	s=e.get()
	w=e.get()
	if a==1:
		r=int(s)+int(w)
		messagebox.showinfo('sum is ',str(r))
def S():
	s=e.get()
	w=e.get()
	if a==1:
		r=int(s)-int(w)
		messagebox.showinfo('sub is ',str(r))
def M():
	s=e.get()
	w=e.get()
	if a==1:
		r=int(s)*int(w)
		messagebox.showinfo('prod is ',str(r))
def D():
	s=e.get()
	w=e.get()
	if a==1:
		r=int(s)//int(w)
		messagebox.showinfo(' division is ',str(r))



x=Label(t,text="Number 1",bg='yellow',fg='black')
y=Label(t,text="Numbwr2",bg='yellow',fg='black')
x.place(x=100,y=50)
y.place(x=100,y=100)

e=Entry(t,bg='pink',fg='blue')
e.place(x=150,y=50)
e1=Entry(t,bg='pink',fg='blue')

e1.place(x=150,y=100)

e1=Button(t,text='sum',bg='blue',command=Cal)
e2=Button(t,text='sub',bg='blue',command=M)
e1.place(x=280,y=180)
e2.place(x=350,y=180)
e4=Button(t,text='mul',bg='blue',command=S)
e5=Button(t,text='divide',bg='blue',command=D)
e4.place(x=280,y=250)
e5.place(x=350,y=250)

c1=Button(t,text='Total')
c1.place(x=280,y=180)


t.mainloop()