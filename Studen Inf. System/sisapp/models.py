from django.db import models

# Create your models here.

class SIS(models.Model):
	enqno=models.IntegerField()
	firstName=models.CharField(max_length=20)
	address=models.CharField(max_length=20)
	email=models.CharField(max_length=30)
	Intrest=models.CharField(max_length=20)
	source=models.CharField(max_length=20)
	birthDate=models.CharField(max_length=20)
	phoneNumber=models.IntegerField()
	refrence=models.CharField(max_length=20)
	gender=models.CharField(max_length=20)
	#female=models.CharField(max_length=20)
	class Meta:
		db_table="SIS"
