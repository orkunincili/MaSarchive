from django.db import models
from django.urls import reverse






class Book(models.Model):
      READ = (
            ('R', 'Read'),
            ('nR', 'NotRead'),

      )
      FAVORITE = (

            ('F','Add My Favorites'),

      )
      book_name=models.CharField(max_length=50)
      author_name=models.CharField(max_length=25,blank=True)
      notes=models.TextField(blank=True)
      date=models.DateTimeField(auto_now_add=True)
      read=models.CharField(max_length=2,choices=READ,default='nR')
      favorite_book=models.CharField(max_length=1,choices=FAVORITE,blank=True)
      book=models.FileField(null=True,blank=True)
      book_path=models.CharField(max_length=100 ,blank=True)

      def get_absolute_url(self):
            return reverse('book:book_detail', kwargs={'id': self.id})




      def __str__(self):

         return self.book_name

      class Meta:
            ordering = ['favorite_book', 'date','id']


class add_multiple(models.Model):
    path = models.CharField(max_length=100)