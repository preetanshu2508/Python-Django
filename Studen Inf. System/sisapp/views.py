from django.shortcuts import render
from django.http import HttpResponse
from sisapp.models import SIS
from django.views.decorators.csrf import csrf_exempt
import smtplib
# Create your views here.

def my(request):
		return render(request,"login.html",{})
def enq(request):
		return render(request,"enquiry.html",{})
@csrf_exempt
def save(request):
	if request.method=="POST":
		a=request.POST['enqno']
		b=request.POST['firstName']
		c=request.POST['address']
		d=request.POST['email']
		e=request.POST['Intrest']
		f=request.POST['source']
		g=request.POST['birthDate']
		h=request.POST['phoneNumber']
		i=request.POST['refrence']
		j=request.POST['gender']
		#k=request.POST.get['male']
		stm=(a+b+c+d+e+f+g+h+i+j)
		
	s=smtplib.SMTP('smtp.gmail.com',587)
	s.starttls()
	s.login('preetanshushukla1125@gmail.com','hemu@2504')
	message=str(a)
	s.sendmail('preetanshushukla1125@gmail.com',d,message)
	s.quit()
	st=SIS(enqno=a,firstName=b,address=c,email=d,Intrest=e,source=f,birthDate=g,phoneNumber=h,refrence=i,gender=j)
	st.save()
	return HttpResponse("<h1>DataSaved for SIS")

def showenq(request):
	enqdata=SIS.objects.all()
	context={'enqdata':enqdata}
	return render(request,'enqshow.html',context)


def test(request,rollno):
	return HttpResponse("<h1> Welcome to my site</h1>"+str(rollno))
####################################################################################################################################
@csrf_exempt
def configcourse(request):
	dataobj=courseadd.objects.all()
	context={'alldata':dataobj}
	return
	render(request,'courseshow.html',context)
@csrf_exempt
def findcourse(request):
	obj=courseadd.objects.filter(Course_ID=cid)
	context={'alldata':obj}
	return
	render(request,'courseupdate.html',context)

def main(request):
		return render(request,"adminenq.html",{})