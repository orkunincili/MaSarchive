from django.db import models
from django.urls import reverse


# Create your models here.
class Diary(models.Model):

      title=models.CharField(max_length=50)
      content=models.TextField()
      date=models.DateTimeField()




class add_multiple(models.Model):

      path=models.CharField(max_length=100)
