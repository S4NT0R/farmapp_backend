from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):

    account_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    typedni= models.CharField('Typedni', max_length = 25)
    dni = models.CharField('Dni', max_length= 15)
    name = models.CharField('Name', max_length = 30)
    lastname = models.CharField('Lastname', max_length= 30)
    eps = models.CharField('Eps', max_length=40)
    gender = models.CharField('Gender', max_length= 20)
    address = models.CharField('Address',max_length=50)
    telephone = models.CharField('Telephone', max_length= 15)

class Deliver(models.Model):

    deliver_id = models.AutoField(primary_key=True) 
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)
    typedni= models.CharField( max_length = 25)
    dni = models.CharField( max_length= 15)
    name = models.CharField( max_length = 30)
    lastname = models.CharField( max_length= 30)
    gender = models.CharField( max_length= 20)
    address = models.CharField(max_length=50)
    telephone = models.CharField( max_length= 15)


class Delivery(models.Model):
     delivery_id = models.AutoField(primary_key=True)
     user_id=models.ForeignKey(User, on_delete=models.CASCADE)
     deliver_id= models.ForeignKey(Deliver, on_delete=models.CASCADE)
     address = models.CharField(max_length=40)
     details = models.TextField()

    


