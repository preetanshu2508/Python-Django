import tkinter 
from tkinter  import*
t=tkinter.Tk()
def S():
	g=s1.get()
	l.config(font=("Arial",g))





l=Label(t,text="preetanshu",fg='blue')


l.place(x=100,y=50)
l.config(font=("Arial",20))
s1=Spinbox(t,from_=0,to_=100,command=S)
s1.place(x=100,y=150)
t.mainloop()


'''
v=Entry(t)
v.place(x=900,y=250)
v1=Entry(t)
v1.place(x=900,y=300)
v2=Entry(t)
v2.place(x=900,y=350)
v3=Entry(t)
v3.place(x=900,y=400)
v4=Entry(t)
v4.place(x=900,y=450)
'''