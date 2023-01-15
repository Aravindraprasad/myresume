from django.db import models

# Create your models here.

class Destination(models.Model):

    name  = models.CharField(max_length=100)
    last  = models.CharField(max_length=100 , null = True)
    img   = models.ImageField(upload_to='pics')
    desc  = models.TextField()
    price = models.IntegerField()

class Review(models.Model):
    name  = models.CharField(max_length=100 , default='' , null=False) 
    email = models.CharField(max_length=100 , default='' , null=False)
    desc = models.CharField(max_length=100 , default='' , null=False)

