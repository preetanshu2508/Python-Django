import tkinter
from tkinter import *
from tkinter import messagebox
import smtplib
import pymysql
import random
import arrow

class sis():
	def __init__(self):
		
		self.sis=tkinter.Tk()

		self.frame=Frame(self.sis,bg='grey',width=1600,height=150)
		self.frame.pack(side=TOP)
		self.sl1=Label(self.sis,text='Registration Form',bg='white',fg='black',font=('arial',40))
		self.sl1.place(x=500,y=25)
		

		self.sf=Frame(self.sis,width=900,height=450,bg='black')
		self.sf.place(x=240,y=150)

#LABELS-LEFT
	
		self.enq=Label(self.sis,text='Enquiry No.',bg='grey',fg='white',font=('arial',20))
		self.enq.place(x=400,y=200)

		self.or1=Label(self.sis,text='OR',bg='grey',fg='white',font=('arial',20))
		self.or1.place(x=600,y=300)

		self.name=Label(self.sis,text='Name',bg='grey',fg='white',font=('arial',20))
		self.name.place(x=400,y=400)

		self.phone=Label(self.sis,text='Phone No.',bg='grey',fg='white',font=('arial',20))
		self.phone.place(x=400,y=500)
#ENTRIES-LEFT

		self.eenq=Entry(self.sis,text='',width=12,bg='white',font=('arial',20),bd=6,relief='sunken')
		self.eenq.place(x=600,y=200)
		self.renq=self.eenq.get()

		
		self.ename=Entry(self.sis,bg='white',width=13,font=('arial',20),bd=6,relief='sunken')
		self.ename.place(x=600,y=400)

		
		self.ephone=Entry(self.sis,bg='white',width=13,font=('arial',20),bd=6,relief='sunken')
		self.ephone.place(x=600,y=500)

#Button
		self.rbtn=Button(self.sis, text='Register',bg='grey',fg='white',font=('arial',15),command=self.reg)
		self.rbtn.place(x=530,y=625)


		self.sis.config(bg='white')
		self.sis.geometry("600x300+350+200")
		self.sis.mainloop()

	def reg(self):
		self.renq=self.eenq.get()
		self.db=pymysql.connect("localhost","root","root","sis")
		self.cur=self.db.cursor()
		self.st="select enquiry_no from enquiry"
		self.cur.execute(self.st)
		self.data=self.cur.fetchall()
		for self.row in self.data:
			
			if self.renq==self.row[0]:
				print('match')
				messagebox.showerror("Saved")
				self.update()
			else:
				print('no')
				messagebox.showerror("Warning")
		self.cur.close()
	def update(self):
		self.db=pymysql.connect("localhost","root","root","sis")
		self.cur=self.db.cursor()
		self.st="select * from enquiry"
		self.cur.execute(self.st)
		self.data=self.cur.fetchall()
		for self.row in self.data:
			self.reg_no='R'+self.row[0]
			self.name=self.row[1]
			self.add=self.row[2]
			self.mob=self.row[3]
			self.email=self.row[4]
			self.int=self.row[5]
			self.src=self.row[6]
			self.ref=self.row[7]
			self.date=self.row[8]
			self.status=self.row[9]
		self.cur.close()

		self.db=pymysql.connect("localhost","root","root","sis")
		self.cur=self.db.cursor()
		self.st="insert into registration values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(self.reg_no,self.name,self.add,self.mob,self.email,self.int,self.src,self.ref,self.date,self.status)
		self.cur.execute(self.st)
		self.db.commit()
		self.cur.close()
		
a=sis()