from django.conf.urls import url
from .views import *

app_name = "book"

urlpatterns = [


        url(r'^book_index/$',book_index),
        url(r'^(?P<id>\d+)/$',book_detail,name="book_detail"),
        url(r'^book_create/$', book_create),
        url(r'^book_update/$',book_update),
        url(r'^book_delete/$', book_delete),
        url(r'^add_book/$',add_multiple_book),


]
