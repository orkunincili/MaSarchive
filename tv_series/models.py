from django.db import models

from django.urls import reverse

# Create your models here.

class Tv_Series(models.Model):

    tv_name = models.CharField(max_length=100,blank=True)
    tv_category=models.CharField(max_length=100,blank=True)
    tv_rate=models.CharField(max_length=5,blank=True)
    tv_poster=models.CharField(max_length=200,blank=True)
    tv_duration=models.CharField(max_length=10,blank=True)
    imdb_page=models.CharField(max_length=200,blank=True)
    tv_summary=models.TextField(blank=True)
    seasons_number=models.IntegerField(blank=True)


    def __str__(self):
        return self.tv_name


    def get_absolute_url(self):
        return reverse('tv_series:tv_detail', kwargs={'id': self.id})

    def get_create_url(self):
        return reverse('tv:tv_create', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('tv:tv_update', kwargs={'id': self.id})



    class Meta:
        ordering = ['-id']



class Tv(models.Model):
    WATCH = (
        ('W', 'Watch'),
        ('nW', 'NotWatch'),

    )
    FAVORITE = (

        ('F', 'Add My Favorites'),

    )

    tv_name=models.ForeignKey('tv_series.Tv_Series',related_name='episodes',on_delete=models.CASCADE)
    season_episode = models.CharField(max_length=7, blank=True)
    episode_name = models.CharField(max_length=100,blank=True)
    favorite_tv = models.CharField(max_length=1, choices=FAVORITE, blank=True)
    tv_path=models.CharField(max_length=200,blank=True)
    poster = models.CharField(max_length=200,blank=True)
    tv_rate=models.CharField(max_length=7,blank=True)
    imdb_page=models.CharField(max_length=100,blank=True)
    duration=models.CharField(max_length=10,blank=True)
    episode_summary=models.TextField(blank=True)
    season=models.IntegerField(blank=True)

    def __str__(self):
        return self.episode_name








class add_multiple(models.Model):
    path = models.CharField(max_length=100)
