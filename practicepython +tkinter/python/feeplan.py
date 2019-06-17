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

#LABELS-LEFT
	
		self.c=Label(self.sis,text='Course_Id',bg='grey',fg='white',font=('arial',20))
		self.c.place(x=50,y=100)

		self.i1=Label(self.sis,text='Installment1',bg='grey',fg='white',font=('arial',20))
		self.i1.place(x=50,y=175)

		self.i2=Label(self.sis,text='Installment2',bg='grey',fg='white',font=('arial',20))
		self.i2.place(x=50,y=250)

		self.i3=Label(self.sis,text='Installment3',bg='grey',fg='white',font=('arial',20))
		self.i3.place(x=50,y=325)

		self.i4=Label(self.sis,text='Installment4',bg='grey',fg='white',font=('arial',20))
		self.i4.place(x=50,y=400)

		self.i5=Label(self.sis,text='Installment5',bg='grey',fg='white',font=('arial',20))
		self.i5.place(x=50,y=475)

#Entry

		self.ci=Entry(self.sis,bg='white',fg='black',font=('arial',20))
		self.ci.place(x=500,y=100)
		
		self.ei1=Entry(self.sis,bg='white',fg='black',font=('arial',20))
		self.ei1.place(x=500,y=175)
		

		self.ei2=Entry(self.sis,bg='white',fg='black',font=('arial',20))
		self.ei2.place(x=500,y=250)
		

		self.ei3=Entry(self.sis,bg='white',fg='black',font=('arial',20))
		self.ei3.place(x=500,y=325)
		self.ei3.insert(0,'0')
		self.ei4=Entry(self.sis,bg='white',fg='black',font=('arial',20))
		self.ei4.place(x=500,y=400)
		

		self.ei5=Entry(self.sis,bg='white',fg='black',font=('arial',20))
		self.ei5.place(x=500,y=475)
		

		

		


#Button
		self.sbtn=Button(self.sis,text='Save',bg='grey',fg='black',font=('arial',15),command=self.save)
		self.sbtn.place(x=500,y=570)


		self.sis.config(bg='black')
		self.sis.geometry("600x300+350+200")
		self.sis.mainloop()
	def save(self):
		self.c=self.ci.get()
		self.i1=self.ei1.get()
		self.i2=self.ei2.get()
		self.i3=self.ei3.get()
		self.i4=self.ei4.get()
		self.i5=self.ei5.get()
		if self.c=='' or self.i1=='' or self.i2=='' or self.i3=='' or self.i4=='':
			messagebox.showerror("Warning","All Fields Are Mandatory")
		else:
			self.db=pymysql.connect("localhost","root","root","sis")
			self.cur=self.db.cursor()
			self.st="insert into feeplan values('%s','%s','%s','%s','%s','%s')"%(self.c,self.i1,self.i2,self.i3,self.i4,self.i5)
			self.cur.execute(self.st)
			self.db.commit()
			self.cur.close()
			messagebox.showinfo("saved",'Saved Successfully')

a=sis()