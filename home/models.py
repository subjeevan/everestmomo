from django.db import models

# Create your models here.

class FoodMenu(models.Model):
    dishname=models.CharField(max_length=100)
    type=models.CharField(max_length=20)
    price=models.IntegerField()
    dishimage=models.ImageField(upload_to='dish')

class Contact(models.Model):
    fname=models.CharField(max_length=10)
    lname=models.CharField(max_length=10)
    email=models.EmailField()
    mobile=models.IntegerField()  
    message=models.CharField(max_length=50)

class Review(models.Model):
    name=models.CharField(max_length=10)
    message=models.CharField(max_length=10)
    date=models.DateTimeField()

class Orgainfo(models.Model):
    organame=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    email=models.EmailField()
    landline=models.IntegerField()  
    mobile=models.IntegerField()  
    altmobile=models.IntegerField()  
    message=models.CharField(max_length=50)