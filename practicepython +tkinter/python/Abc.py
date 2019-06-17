import tkinter
from tkinter import*
from tkinter import messagebox
t=tkinter.Tk()
s=IntVar()
v=IntVar()
l=IntVar()

def Cal():
	s=s1.get()
	v=int(s)*100
	p2.config(text=v)
	return v
def C():
	w=s2.get()
	n=int(w)*40
	p3.config(text=n)
	return n
def D():
	sr=s3.get()
	k=int(sr)*50
	p4.config(text=k)
	return k
def E():
	st=s4.get()
	vc=int(st)*40
	p5.config(text=vc)
	return vc
def F():
	vt=s5.get()
	vm=int(vt)*80
	p6.config(text=vm)
	return vm
def Sum():
	c=Cal()
	b1=C()
	b2=D()
	b3=E()
	b4=F()
	l=c+b1+b2+b3+b4
	p7.config(text=l)





l=Label(t,text="Abc Shop",fg='black')


l.place(x=540,y=20)
l.config(font=("Arial",30))
l1=Label(t,text="Enter your name")
l1.config(font=("Arial",10))
l1.place(x=300,y=100)
e=Entry(t)
e.place(x=600,y=100)
l2=Label(t,text="Product")
l2.config(font=("Arial",10))
l2.place(x=300,y=200)
e1=Entry(t)
e1.place(x=300,y=250)
e2=Entry(t)
e2.place(x=300,y=300)
e3=Entry(t)
e3.place(x=300,y=350)
e4=Entry(t)
e4.place(x=300,y=400)
e4=Entry(t)
e4.place(x=300,y=450)

l3=Label(t,text="Quantity")
l3.config(font=("Arial",10))
l3.place(x=600,y=200)

s1=Spinbox(t,from_=0,to_=5,command=Cal)
s1.place(x=600,y=250)
s2=Spinbox(t,from_=0,to_=5,command=C)
s2.place(x=600,y=300)
s3=Spinbox(t,from_=0,to_=5,command=D)
s3.place(x=600,y=350)
s4=Spinbox(t,from_=0,to_=5,command=E)
s4.place(x=600,y=400)
s5=Spinbox(t,from_=0,to_=5,command=F)
s5.place(x=600,y=450)

l4=Label(t,text="Price")

l4.place(x=900,y=200)
l5=Label(t,text='100')

l5.place(x=900,y=250)
l6=Label(t,text='40')
l6.place(x=900,y=300)
l7=Label(t,text=50)
l7.place(x=900,y=350)
l8=Label(t,text='40')
l8.place(x=900,y=400)
l9=Label(t,text=50)
l9.place(x=900,y=450)

p1=Label(t,text="Total")

p1.place(x=1100,y=200)

p2=Label(t)
p2.place(x=1100,y=250)
p3=Label(t)
p3.place(x=1100,y=300)
p4=Label(t)
p4.place(x=1100,y=350)
p5=Label(t)
p5.place(x=1100,y=400)
p6=Label(t)
p6.place(x=1100,y=450)

p7=Label(t)
p7.place(x=1100,y=650)








c1=Button(t,text='Total',command=Sum)
c1.place(x=650,y=600)






t.mainloop()