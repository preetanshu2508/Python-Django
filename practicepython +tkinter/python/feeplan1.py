import numpy as np 
import pandas as pd 
import tkinter 
from tkinter import ttk
from tkinter import *
t = tkinter.Tk()
t.geometry('1366x768')

#Labels......
lbl1 = Label(t,text='Course ID : ')
lbl1.place(x=200,y=200)

lbl2 = Label(t,text='Course Name : ')
lbl2.place(x=200,y=250)

lbl3 = Label(t,text='Total fees : ')
lbl3.place(x=200,y=300)

lbl4 = Label(t,text='Duration : ')
lbl4.place(x=200,y=350)

lbl5 = Label(t,text='FeePlan ID : ')
lbl5.place(x=200,y=400)

#Entries.........

ent3 = Label(t,text='',bg='red',width=20)
ent3.place(x=300,y=300)

ent1 = Entry(t)
ent1.place(x=300,y=200)
cbo1 = ttk.Combobox(t)
cbo1['values'] = ("Python","Java","C","C++","Ruby","Android","Sql","Vb.Net")
#g = cbo1.get("Python")
if cbo1=="Python":
	ent3.config(t,text="2000")

cbo1.place(x=300,y=250)


ent4 = Entry(t)
ent4.place(x=300,y=350)

cbo2 = ttk.Combobox(t)
cbo2.place(x=300,y=400)

lst = Listbox(t)



btn = Button(t,text='Save')
btn.place(x=200,y=450)
t.mainloop()