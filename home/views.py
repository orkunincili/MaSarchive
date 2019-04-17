from django.shortcuts import render,HttpResponseRedirect
from .models import User
from .forms import UserForm
from book.models import Book
from movie.models import Movie
from django.contrib import messages
# Create your views here.




def home_view(request):

    setting=User.objects.all()
    books=Book.objects.all().count()
    movies=Movie.objects.all().count()

    context={

        "setting":setting,
        "books":books,
        "movies":movies,
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