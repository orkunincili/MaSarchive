from django.db import models
from django.urls import reverse
# Create your models here.
class User(models.Model):
    SELECT = (
        ('E', 'Enable'),
        ('D', 'Disable'),

    )

    user_name=models.CharField(max_length=22,blank=True)
    movie=models.CharField(max_length=20,blank=True)
    select_movie = models.CharField(max_length=1, choices=SELECT, default='E')
    blog=models.CharField(max_length=20,blank=True)
    select_blog = models.CharField(max_length=1, choices=SELECT, default='E')
    book=models.CharField(max_length=20,blank=True)
    select_book = models.CharField(max_length=1, choices=SELECT, default='E')




    def __str__(self):
       return self.user_name

