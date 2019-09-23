from django.db import models
from django.contrib.auth.models import User

class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField(max_length=100)
    price = models.IntegerField()
	



class signup(models.Model):
	username = models.CharField(max_length=100)
	firstname = models.CharField(max_length=100)
	lastname = models.CharField(max_length=100)
	email =  models.CharField(max_length=100)
	password = models.CharField(max_length=100)

    
	def __str__(self):
		return self.username
