from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect,redirect,Http404
from .models import Movie
from home.models import User
from .forms import MovieForm,add_multipleForm
from django.contrib import messages
import os,magic,webbrowser

# Create your views here.
def movie_index(request):
    movies=Movie.objects.all()
    user=User.objects.all()
    movieW=[]
    movieNW=[]
    favorite_movies=[]

    for i in movies:
        if (i.favorite_movie=="F"):
            favorite_movies.append(i)

        elif(i.watch=="W"):
            movieW.append(i)

        else:
            movieNW.append(i)
    len_fav=len(favorite_movies)
    len_W=len(movieW)
    len_nW=len(movieNW)
    context={
        "movieW":movieW,
        "movieNW":movieNW,
        "user":user,
        "fav_movie":favorite_movies,
        "movies":movies,
        "len_fav":len_fav,
        "len_W":len_W,
        "len_nW":len_nW,
    }

    return render(request,"movies/movie_index.html",context)
def movie_create(request):
    form = MovieForm(request.POST or None)
    user = User.objects.all()
    if form.is_valid():
        movie = form.save(commit=False)

        movie.save()

    context = {
        'form': form,
        'user': user,
    }

    return render(request, "movies/movies_form.html", context)







def movie_update(request,id):
    movie = Movie.objects.get(id=id)
    user = User.objects.all()
    form = MovieForm(request.POST or None, request.FILES or None, instance=movie)
    if form.is_valid():
        form.save()
        messages.success(request, "Başarılı bir şekilde güncellediniz.")

        return HttpResponseRedirect(movie.get_absolute_url())
    context = {
        'form': form,
        'user': user,
    }


    return render(request, "movies/movies_form.html", context)
def movie_detail(request,id):
    movie=Movie.objects.get(id=id)
    user = User.objects.all()
    webbrowser.open(movie.movie_path)

    context={
        "movieD":movie,
        "user":user,

    }

    return render(request,"movies/movie_detail.html",context)


def add_multiple_movie(request):

    form = add_multipleForm(request.POST or None)
    user=User.objects.all()
    file_list=[]
    movie_list=[]
    if form.is_valid():
        path = form.save()


        for root,dirs,files in os.walk(path.path):
            for file in files:
                file_list.append(os.sep.join([root,file]))

        for i in range(len(file_list)):

            mime_type=magic.from_file(file_list[i],mime=True)

            if mime_type.startswith("video")==True:
                movie_list.append(file_list[i].split("/")[-1])

        for i in movie_list:


          Movie.objects.create(movie_name=i,movie_path="file://"+path.path+"/"+i)



    context = {
        'form': form,
        'user':user,
    }

    return render(request, "movies/add_movie.html", context)