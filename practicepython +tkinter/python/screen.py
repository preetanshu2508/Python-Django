import tkinter 
from tkinter  import*

t=tkinter.Tk()
lt=Listbox()
lt.insert(1,"Agra")
lt.insert(2,"Allahabad")
lt.insert(3,"lucknow")
lt.insert(4,"firozabaad")
lt.place(x=50,y=50)
x=IntVar()
r=Radiobutton(t,text='Male',variable=x,value=1)
r2=Radiobutton(t,text='Female',variable=x,value=1)
r.place(x=200,y=80)
r2.place(x=200,y=100)
y=IntVar()
c1=Checkbutton(t,text='Reading',variable='y',onvalue=1,offvalue=2)
c2=Checkbutton(t,text='Singing',variable='y',onvalue=1,offvalue=2)
c1.place(x=300,y=80)
c2.place(x=300,y=100)
e=Button(t,text='Submit',bg='red')
e1=Button(t,text='Review',bg='blue')
e1.place(x=400,y=80)
e.place(x=400,y=100)
v=DoubleVar()
s=Scale(t,variable=v)
s.place(x=400,y=200)
s1=Spinbox(t,from_=0,to_=100)
s1.place(x=500,y=250)
t.mainloop()