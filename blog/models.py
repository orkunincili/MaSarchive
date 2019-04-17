from django.db import models
from django.urls import reverse


# Create your models here.
class Diary(models.Model):

      title=models.CharField(max_length=50)
      content=models.TextField()
      date=models.DateTimeField(auto_now=True)

      def __str__(self):
            return self.title



      def get_absolute_url(self):
            return reverse('blog:blog_detail', kwargs={'id': self.id})

      def get_create_url(self):
            return reverse('blog:blog_create', kwargs={'id': self.id})

      def get_update_url(self):
            return reverse('blog:blog_update', kwargs={'id': self.id})

      class Meta:
            ordering = ['-date', 'id']



