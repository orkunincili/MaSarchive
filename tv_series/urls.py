from django.conf.urls import url
from .views import *
from home.models import User


app_name = "tv_series"
urlpatterns = [


        url(r'^tv_index/$', tv_index),
        url(r'^tv_create/$', tv_create),
        url(r'^(?P<id>\d+)/$', tv_detail, name="tv_detail"),
        url(r'^add_tv/$', add_multiple_tv),

   ]