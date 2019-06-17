import numpy as np 
import pandas as pd 
import tkinter
from tkinter import *
import pymysql
from tkinter import messagebox




class sis():
	def __init__(self):
		
		self.sis=tkinter.Tk()

		self.frame=Frame(self.sis,bg='black',width=2000,height=200)
		self.frame.pack(side=TOP)
		self.sl1=Label(self.sis,text='FEE PLAN',bg='white',fg='black',font=('arial',25))
		self.sl1.place(x=600,y=20)
		

		self.sf=Frame(self.sis,width=1000,height=650,bg='black')
		self.sf.place(x=240,y=150)
		self.sis.mainloop()

	def show():
		elf.db=pymysql.connect("localhost","root","root","sis")
		self.cur=self.db.cursor()
		self.st="select * from feeplan"
		self.cur.execute(self.st)
		self.data=self.cur.fetchall()
		for self.row in self.data:
			Label(self.sis,text=self.row[1]).grid(row=index,column=0)
			Label(self.sis,text=self.row[2]).grid(row=index,column=1)
			Label(self.sis,text=self.row[3]).grid(row=index,column=2)
			index+=1

		self.cur.close()
		self.sis.mainloop()
a=sis()

