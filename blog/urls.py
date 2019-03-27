
from django.conf.urls import url
from .views import *

app_name = "blog"
urlpatterns = [


    url(r'^blog_index/$',book_index),
    url(r'^(?P<id>\d+)/$',book_detail,name="blog_detail"),
    url(r'^blog_create/$', book_create),
    url(r'^blog_update/$',book_update),
    url(r'^blog_delete/$', book_delete),





]





