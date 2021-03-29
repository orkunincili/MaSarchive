from django.shortcuts import render,HttpResponse
from .models import User
from .forms import UserForm
from book.models import *
from movie.models import Movie
from tv_series.models import *
import random

# Create your views here.




def home_view(request):
    setting = User.objects.all()
    books = Book.objects.filter(read="Rg")
    movies = Movie.objects.all()
    len_m = Movie.objects.all().count()

    tv_series = Tv_Series.objects.all()
    len_tv = Tv_Series.objects.all().count()









    context={
        
        "random_tv": tv_series,

        "setting": setting,
        "books": books,
        "movies": movies,
        "tv_series": tv_series,
        "rane": range(4),

    }


    return render(request,"home/home.html",context)



def user_settings(request):
    user = User.objects.all()
    if user.count()!=0:
        form=UserForm(request.POST or None,instance=user[0])
    else:
        form = UserForm(request.POST or None)

    if form.is_valid():
        setting = form.save()



        if(user.count()>1):
            User.objects.get(id=setting.id-1).delete()


    return render(request,"home/user_settings.html",{"form":form})
