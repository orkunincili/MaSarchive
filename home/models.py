from django.db import models
from django.urls import reverse
# Create your models here.
class User(models.Model):

    user_name=models.CharField(max_length=22,blank=True)
    tv_series=models.CharField(max_length=20,blank=True)
    movie=models.CharField(max_length=20,blank=True)
    blog=models.CharField(max_length=20,blank=True)
    book=models.CharField(max_length=20,blank=True)



    def __str__(self):
       return self.user_name

