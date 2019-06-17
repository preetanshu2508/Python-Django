
import tkinter
from tkinter import *
from tkinter import messagebox
import smtplib
import pymysql
import random
import arrow

class sis():
	p=''
	m=''
	def __init__(self):

		self.sis=tkinter.Tk()

		self.frame=Frame(self.sis,bg='grey',width=1600,height=150)
		self.frame.pack(side=TOP)
		self.sl=Label(self.sis,text='Student Enquiry System',bg='white',fg='black',font=('arial',60))
		self.sl.place(x=265,y=25)

		self.sf=Frame(self.sis,width=900,height=450,bg='black')
		self.sf.place(x=240,y=150)

#LABELS-LEFT
	
		self.enq=Label(self.sis,text='Enquiry No.',bg='grey',fg='white',font=('arial',20))
		self.enq.place(x=300,y=200)

		self.name=Label(self.sis,text='Name',bg='grey',fg='white',font=('arial',20))
		self.name.place(x=300,y=300)

		self.add=Label(self.sis,text='Address',bg='grey',fg='white',font=('arial',20))
		self.add.place(x=300,y=400)

		self.mob=Label(self.sis,text='Mobile No.',bg='grey',fg='white',font=('arial',20))
		self.mob.place(x=300,y=500)
#ENTRIES-LEFT

		self.eenq=Label(self.sis,text='',width=12,bg='white',font=('arial',20),bd=6,relief='sunken')
		self.eenq.place(x=470,y=200)

		self.ename=Entry(self.sis,bg='white',width=13,font=('arial',20),bd=6,relief='sunken')
		self.ename.place(x=468,y=300)

		self.eadd=Entry(self.sis,bg='white',width=13,font=('arial',20),bd=6,relief='sunken')
		self.eadd.place(x=468,y=400)

		self.emob=Entry(self.sis,bg='white',width=13,font=('arial',20),bd=6,relief='sunken')
		self.emob.place(x=468,y=500)
#LABELS-RIGHT

		self.mail=Label(self.sis,text='E-Mail ID.',bg='grey',fg='white',font=('arial',20))
		self.mail.place(x=750,y=200)

		self.intr=Label(self.sis,text='Interest',bg='grey',fg='white',font=('arial',20))
		self.intr.place(x=750,y=300)

		self.sorc=Label(self.sis,text='Source',bg='grey',fg='white',font=('arial',20))
		self.sorc.place(x=750,y=400)

		self.ref=Label(self.sis,text='Reference',bg='grey',fg='white',font=('arial',20))
		self.ref.place(x=750,y=500)
#ENTRIES-RIGHT

		self.email=Entry(self.sis,bg='white',width=13,font=('arial',20),bd=6,relief='sunken')
		self.email.place(x=880,y=195)

		self.eintr=Entry(self.sis,bg='white',width=13,font=('arial',20),bd=6,relief='sunken')
		self.eintr.place(x=880,y=295)

		self.esorc=Entry(self.sis,bg='white',width=13,font=('arial',20),bd=6,relief='sunken')
		self.esorc.place(x=880,y=395)

		self.eref=Entry(self.sis,bg='white',width=13,font=('arial',20),bd=6,relief='sunken')
		self.eref.place(x=880,y=495)

		self.svbtn=Button(self.sis,text='Save',bg='grey',fg='white',font=('arial',15),command=self.save)
		self.svbtn.place(x=530,y=625)

		self.cnclbtn=Button(self.sis,text='Cancel',bg='grey',fg='white',font=('arial',15),command=self.cnclbtn)
		self.cnclbtn.place(x=800,y=625)

		'''self.cn=Button(self.sis,text='Confirm OTP',bg='grey',fg='white',font=('arial',10),relief='flat')
		self.cn.place(x=650,y=570)'''

		self.sis.config(bg='white')
		self.sis.geometry("1600x800")
		self.sis.mainloop()

	def cnclbtn(self):
		self.sis.destroy()

	def save(self):
		self.nm=self.ename.get().title()
		self.ad=self.eadd.get().title()
		self.mon=self.emob.get()
		self.mid=self.email.get()
		self.i=self.eintr.get().capitalize()
		self.sor=self.esorc.get().capitalize()
		self.refr=self.eref.get().capitalize()
		self.sts='N'


		if self.nm=='' or self.ad=='' or self.mon=='' or self.mid=='' or self.i=='' or self.sor=='' or self.refr=='':
			messagebox.showerror("Warning","All Fields Are Mandatory")
		else:
			self.db=pymysql.connect("localhost","root","root","sis")
			self.cur=self.db.cursor()
			self.st="select Enquiry_No from enquiry"
			self.cur.execute(self.st)
			self.data=self.cur.fetchall()
			for self.e in self.data:
					self.p=(self.e[0][8:])
					self.m=(self.e[0][:8])
			print('p  ',self.p) 	#sequence
			print('m  ',self.m)	    #date
			
			self.now=arrow.now().format('YYYYMMDD')
			#print(self.now)

			if self.m!=self.now:		#date compare
				self.f='01'
				#print(self.f)
			else:
				self.f=int(self.p)+1
				print('f   ',self.f)
			
			if self.p>'09' or self.p>'9':
				self.enqno=str(self.now)+str(self.f)
			else:
				self.enqno=str(self.now)+'0'+str(self.f)	

			self.eenq.config(text=self.enqno)
			
			self.s=smtplib.SMTP('smtp.gmail.com',587)
			self.s.starttls()
			self.s.login('preetanshushukla1125@gmail.com','hemu@2504')
			self.message=str(self.enqno)
			self.s.sendmail('preetanshushukla1125@gmail.com',self.mid,self.message)
			self.s.quit()
			print('sent')

			self.d=arrow.now().format('DD/MM/YYYY')
			self.db=pymysql.connect("localhost","root","root","sis")
			self.cur=self.db.cursor()
			self.st="insert into enquiry values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(self.enqno,self.nm,self.ad,self.mon,self.mid,self.i,self.sor,self.refr,self.d,self.sts)
			self.cur.execute(self.st)
			self.db.commit()
			print('saved')
			messagebox.showinfo("Success","Save Successfully..!!")

           '''
			self.eenq.config(text='')
			self.ename.delete(0,END)
			self.eadd.delete(0,END)
			self.emob.delete(0,END)
			self.email.delete(0,END)
			self.eintr.delete(0,END)
			self.esorc.delete(0,END)
			self.eref.delete(0,END)'''

			messagebox.showinfo("Alert","Data Saved Temporary,Please Confirm Your E-Mail Address\nTo Successfully Save Your Data")
			#self.confirm()
			

	def confirm(self):
		self.t=tkinter.Tk()

		self.tf=Frame(self.t,width=400,height=170,bg='grey')
		self.tf.place(x=100,y=50)
		self.tl=Label(self.t,text='Enter OTP',fg='white',bg='grey',font=('arial',20))
		self.tl.place(x=140,y=120)
		self.te=Entry(self.t,bg='white',width=10,font=('arial',20),bd=3,relief='sunken')
		self.te.place(x=300,y=115)
		self.tb=Button(self.t,text='Confirm',bg='grey',font=('arial',15),command=self.cnfrmbtn)
		self.tb.place(x=265,y=240)

		self.t.config(bg='white')
		self.t.geometry("600x300+350+200")
		self.t.mainloop()
'''
	def cnfrmbtn(self):
		self.otp=int(self.te.get())

		if self.otp==self.pin:
			#messagebox.showinfo('hi','found')
			
			self.db2=pymysql.connect("localhost","root","root","sis")
			self.cur2=self.db2.cursor()
			self.st2="delete from temp"
			self.cur2.execute(self.st2)
			self.db2.commit()


			self.d=arrow.now().format('DD/MM/YYYY')
			self.db1=pymysql.connect("localhost","root","root","sis")
			self.cur1=self.db1.cursor()
			self.st1="insert into enquiry values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(self.enqno,self.nm,self.ad,self.mon,self.mid,self.i,self.sor,self.refr,self.d,self.sts)
			self.cur1.execute(self.st1)
			self.db1.commit()
			print('saved1')
			self.t.destroy()
		else:
			messagebox.showinfo('Warning','Invalid OTP')

		
'''

s=sis()
