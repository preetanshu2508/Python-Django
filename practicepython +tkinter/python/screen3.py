import tkinter
from tkinter import*
from tkinter import messagebox

t=tkinter.Tk()
def Hellow():
	messagebox.showinfo('hellow','welcome')
'''w=Canvas(t,width=800,height=600,bg="blue")
w.create_line(200,200,500,200,fill="yellow")

w.create_oval(200,200,500,300,fill="blue")
cord=100,200,200,150
w.create_rectangle(cord,fill="blue")

w.create_polygon(200,400,600,800,300,560,670,540,fill='red')
img=PhotoImage(file='ps.png')
w.create_image(50,100,anchor=NW,image=img)


w.pack()'''
e=Button(t,text='',command=Hellow)
e.place(x=100,y=100)
t.mainloop()