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
		self.sl=Label(self.sis,text='Student Registration System',bg='white',fg='red',font=('arial',60))
		self.sl.place(x=265,y=25)

		self.sf=Frame(self.sis,width=900,height=450,bg='black')
		self.sf.place(x=240,y=150)

#LABELS-LEFT
	
		self.reg=Label(self.sis,text='Registration No.',bg='grey',fg='white',font=('arial',20))
		self.reg.place(x=300,y=200)

		self.name=Label(self.sis,text='Name',bg='grey',fg='white',font=('arial',20))
		self.name.place(x=300,y=300)

		self.phone=Label(self.sis,text='Phone No',bg='grey',fg='white',font=('arial',20))
		self.phone.place(x=300,y=400)


		
#ENTRIES-LEFT

		self.ereg=Entry(self.sis,text='',width=12,bg='white',font=('arial',20),bd=6,relief='sunken')
		self.ereg.place(x=470,y=200)

		self.ename=Entry(self.sis,bg='white',width=13,font=('arial',20),bd=6,relief='sunken')
		self.ename.place(x=468,y=300)

		self.ephone=Entry(self.sis,bg='white',width=13,font=('arial',20),bd=6,relief='sunken')
		self.ephone.place(x=468,y=400)	

		self.regbtn=Button(self.sis,text='Register',bg='grey',fg='white',font=('arial',15),command=self.search)
		self.regbtn.place(x=530,y=625)

		self.sis.config(bg='white')
		self.sis.geometry("1600x800")
		self.sis.mainloop()
'''def save(self):
	    self.nm1=self.ereg.get().title()
		self.nm=self.ename.get().title()
		self.ad=self.eadd.get().title()
		self.mon=self.emob.get()
		self.mid=self.email.get()
		self.i=self.eintr.get().capitalize()
		self.sor=self.esorc.get().capitalize()
		self.refr=self.eref.get().capitalize()
		self.sts='N'''



	def search(self):
		self.db=pymysql.connect("localhost","root","root","sis")
		self.cur=self.db.cursor()
		self.reg=self.ereg.get()
		self.st="select * from enquiry"
		try:
				self.cur.execute(st)
				self.data=cur.fetchall()
				for self.r in self.data:
					if self.r[0]==self.reg:
						print("match")
					else:
						messagebox.showinfo("Kindly first Complete Enquiry ")
		except:
				print("Error!!!")

'''def R():
	self.db=pymysql.connect("localhost","root","root","sis")
	self.cur=self.db.cursor()
	self.st="insert into registration values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(self.nm1,self.nm,self.ad,self.mon,self.mid,self.i,self.sor,self.refr,self.d,self.sts)
	self.cur.execute(self.st)
	self.db.commit()
	print('saved')
	messagebox.showinfo("Success","Save Successfully..!!")'''

s=sis()