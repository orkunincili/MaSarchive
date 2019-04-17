
from django.conf.urls import url
from .views import *
app_name = "blog"


urlpatterns = [


        url(r'^blog_index/$',blog_index),
        url(r'^(?P<id>\d+)/$',blog_detail,name="blog_detail"),
        url(r'^blog_create/$', blog_create),
        url(r'^(?P<id>\d+)/blog_update/$',blog_update,name="blog_update"),
        url(r'^blog_delete/$', blog_delete,name="blog_delete"),
    ]






