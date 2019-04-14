from django.db import models
from django.urls import reverse

# Create your models here.
class Movie(models.Model):
    WATCH = (
        ('W', 'Watch'),
        ('nW', 'NotWatch'),

    )
    FAVORITE = (

        ('F', 'Add My Favorites'),

    )



    movie_name = models.CharField(max_length=50)
    notes = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    watch = models.CharField(max_length=2, choices=WATCH, default='W')
    movie = models.FileField(null=True, blank=True)
    favorite_movie = models.CharField(max_length=1, choices=FAVORITE, blank=True)
    movie_path=models.CharField(max_length=200,blank=True)
    category = models.CharField(max_length=50, blank=True)
    poster = models.CharField(max_length=200,blank=True)
    movie_rate=models.CharField(max_length=5,blank=True)
    imdb_page=models.CharField(max_length=100,blank=True)


    def __str__(self):

        return self.movie_name

    def get_absolute_url(self):
        return reverse('movie:movie_detail', kwargs={'id': self.id})

    def get_create_url(self):
        return reverse('movie:movie_create', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('movie:movie_update', kwargs={'id': self.id})



    class Meta:
        ordering = ['date', 'id']



class add_multiple(models.Model):
    path = models.CharField(max_length=100)