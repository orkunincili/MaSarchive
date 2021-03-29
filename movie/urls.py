from django.conf.urls import url
from personalblog import settings
from .views import *
from home.models import User
from django.conf.urls.static import static

app_name = "movie"
urlpatterns = [

        url(r'^movie_create/$', movie_create),
        url(r'^(?P<id>\d+)/$', movie_detail,name="movie_detail"),
        url(r'^(?P<id>\d+)/movie_update/$', movie_update,name="movie_update"),
        url(r'^add_movie/$',add_multiple_movie),
        url(r'^movies/$',movies),
        
   ]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
