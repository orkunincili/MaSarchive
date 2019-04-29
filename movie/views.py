from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import Movie
from home.models import User
from .forms import MovieForm,add_multipleForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os,magic,webbrowser
from bs4 import BeautifulSoup
import requests
global process
import subprocess


# Create your views here.

def movie_index(request):
    user = User.objects.all()
    if user[0].select_movie == 'E':
        movies = Movie.objects.all()
        user = User.objects.all()
        movieW = []
        movieNW = []
        favorite_movies = []

        for i in movies:
            if (i.favorite_movie == "F"):
                favorite_movies.append(i)

            elif (i.watch == "W"):
                movieW.append(i)

            else:
                movieNW.append(i)

        len_fav = len(favorite_movies)
        len_W = len(movieW)
        len_nW = len(movieNW)
        context = {
            "movieW": movieW,
            "movieNW": movieNW,
            "user": user,
            "fav_movie": favorite_movies,
            "movies": movies,
            "len_fav": len_fav,
            "len_W": len_W,
            "len_nW": len_nW,

        }

        return render(request, "movies/movie_index.html", context)
    else:
        return HttpResponse("App is disable")
def favorite_movie(request):
    user = User.objects.all()
    if user[0].select_movie == 'E':
        movies = Movie.objects.all()
        movieW=Movie.objects.filter(watch="W")
        movieNW=Movie.objects.filter(watch="nW")
        user = User.objects.all()
        favorite_movies=Movie.objects.filter(favorite_movie='F')
        paginator = Paginator(favorite_movies, 21)

        page = request.GET.get('page')
        try:
            movieF = paginator.page(page)
        except PageNotAnInteger:

            movieF = paginator.page(1)
        except EmptyPage:

            movieF = paginator.page(paginator.num_pages)

        len_fav = len(favorite_movies)
        len_W = len(movieW)
        len_nW = len(movieNW)
        context = {
            "movieW": movieW,
            "movieNW": movieNW,
            "user": user,
            "fav_movie": movieF,
            "movies": movies,
            "len_fav": len_fav,
            "len_W": len_W,
            "len_nW": len_nW,

        }

        return render(request, "movies/fav_movies.html", context)
    else:
        return HttpResponse("App is disable")
def didnt_watch(request):
    user = User.objects.all()
    if user[0].select_movie == 'E':
        movies = Movie.objects.all()
        user = User.objects.all()
        movieW = Movie.objects.filter(watch="W")
        movieNW = Movie.objects.filter(watch="nW")
        favorite_movies=Movie.objects.filter(favorite_movie='F')

        paginator = Paginator(movieNW, 21)

        page = request.GET.get('page')
        try:
            movienW = paginator.page(page)
        except PageNotAnInteger:

            movienW = paginator.page(1)
        except EmptyPage:

            movienW = paginator.page(paginator.num_pages)


        len_fav = len(favorite_movies)
        len_W = len(movieW)
        len_nW = len(movieNW)
        context = {
            "movieW": movieW,
            "movieNW": movienW,
            "user": user,
            "fav_movie": favorite_movies,
            "movies": movies,
            "len_fav": len_fav,
            "len_W": len_W,
            "len_nW": len_nW,

        }


        return render(request, "movies/didnt_watch.html", context)
    else:
        return HttpResponse("App is disable")

def watched(request):
    user = User.objects.all()
    if user[0].select_movie == 'E':
        movies = Movie.objects.all()

        user = User.objects.all()
        favorite_movies=Movie.objects.filter(favorite_movie="F")
        movieNW = Movie.objects.filter(watch="nW")
        movieW = Movie.objects.filter(watch="W")

        paginator = Paginator(movieW, 22)
        page = request.GET.get('page')


        try:
            movies_w = paginator.page(page)
        except PageNotAnInteger:

            movies_w = paginator.page(1)
        except EmptyPage:

            movies_w = paginator.page(paginator.num_pages)






        len_fav = len(favorite_movies)
        len_W = len(movieW)
        len_nW = len(movieNW)
        context = {

            "movieW": movies_w,
            "movieNW": movieNW,
            "user": user,
            "fav_movie": favorite_movies,
            "movies": movies,
            "len_fav": len_fav,
            "len_W": len_W,
            "len_nW": len_nW,



        }

        return render(request, "movies/watched.html", context)
    else:
        return HttpResponse("App is disable")

def movie_create(request):
    user = User.objects.all()
    if user[0].select_movie == 'E':

        form = MovieForm(request.POST or None)


        if form.is_valid():
                movie=form.save(commit=False)
                base_url = 'http://www.imdb.com/find'
                imdb = 'http://www.imdb.com'
                params = dict(ref_="nv_sr_fn", q=movie.movie_name, s="tt")

                r = requests.get(base_url, params=params)
                source = BeautifulSoup(r.content, "lxml")
                movie_list = source.find("ul", attrs={"class": "findTitleSubfilterList"}).find("a").get("href")
                r = requests.get(imdb + movie_list)
                source = BeautifulSoup(r.content, "lxml")
                movie_page = source.find("td", attrs={"class": "result_text"}).find("a").get("href")
                movie_detail = requests.get(imdb + movie_page)
                source = BeautifulSoup(movie_detail.content, "lxml")
                if source.find("h1", attrs={"class": ""}) == None:

                    movie_name = source.find("h1", attrs={"class": "long"}).text

                else:
                    movie_name = source.find("h1", attrs={"class": ""}).text
                try:
                    duration = source.find("time").text

                except:
                    duration = "No Duration"
                movie_poster_url = source.find("div", attrs={"class": "poster"}).find("img").get("src")
                new_poster_url = ""
                movie_poster_url = movie_poster_url.split(".")
                del movie_poster_url[-2]

                for i in movie_poster_url:
                    new_poster_url += i
                    if movie_poster_url.index(i) < len(movie_poster_url) - 1:
                        new_poster_url += "."

                movie_poster = new_poster_url
                try:
                   movie_rate = source.find("span", attrs={"itemprop": "ratingValue"}).text
                except:
                   movie_rate="No Rate"
                movie_category = source.find("div", attrs={"class": "subtext"}).find_all("a")
                summary = source.find("div", attrs={"class": "summary_text"}).text

                movie_category_text = ""
                del movie_category[-1]
                for category in movie_category:
                    movie_category_text+=category.text+" "

                movie=Movie.objects.create(movie_name=movie_name, poster=movie_poster,watch=movie.watch,imdb_page=imdb+movie_page,
                                     movie_rate=movie_rate, category=movie_category_text,duration=duration,summary=summary)

                return HttpResponseRedirect(movie.get_absolute_url())

        context = {
            'form': form,
            'user': user,
        }

        return render(request, "movies/movies_form.html", context)

    else:
        return HttpResponse("App is disable")





def movie_update(request,id):
    user = User.objects.all()
    if user[0].select_movie == 'E':
        movie = Movie.objects.get(id=id)
        user = User.objects.all()
        form = MovieForm(request.POST or None, request.FILES or None, instance=movie)
        if form.is_valid():
            form.save()


            return HttpResponseRedirect(movie.get_absolute_url())
        context = {
            'form': form,
            'user': user,
            'movie':movie,
        }


        return render(request, "movies/movies_form.html", context)
    else:
        return HttpResponse("App is disable")

def movie_detail(request,id):
    user = User.objects.all()
    if user[0].select_movie == 'E':
        movie=Movie.objects.get(id=id)
        user = User.objects.all()


        if request.POST.get("Play") == 'Play':
            subprocess.call(['vlc',movie.movie_path])




        context={
            "movieD":movie,
            "user":user,


        }

        return render(request,"movies/movie_detail.html",context)
    else:
        return HttpResponse("App is disable")

def add_multiple_movie(request):
    user = User.objects.all()
    if user[0].select_movie == 'E':
        form = add_multipleForm(request.POST or None)
        user=User.objects.all()
        file_list=[]
        movie_name_list=[]
        movie_path_list=[]
        if form.is_valid():
            path = form.save()


            for root,dirs,files in os.walk(path.path):
                for file in files:
                    file_list.append(os.sep.join([root,file]))

            for i in range(len(file_list)):

                mime_type=magic.from_file(file_list[i],mime=True)

                if mime_type.startswith("video")==True:
                    movie_name_list.append(file_list[i].split("/")[-1])
                    movie_path_list.append(file_list[i])

            for i in range(len(movie_path_list)):
                path=movie_path_list[i]
                movie_name_list[i] = movie_name_list[i].replace(".mp4","")
                movie_name_list[i] = movie_name_list[i].replace(".mkv","")
                movie_name_list[i] = movie_name_list[i].replace(".avi","")

                base_url = 'http://www.imdb.com/find'
                imdb = 'http://www.imdb.com'

                params = dict(ref_="nv_sr_fn",q=movie_name_list[i], s="tt")

                r = requests.get(base_url, params=params)
                source = BeautifulSoup(r.content, "lxml")

                if source.find("td", attrs={"class":"result_text"})==None:
                    params = dict(q=movie_name_list[i],s="tt",ttype="ft",ref_="fn_ft")
                    r = requests.get(base_url, params=params)
                    source = BeautifulSoup(r.content, "lxml")
                movie_page = source.find("td", attrs={"class":"result_text"}).find("a").get("href")
                movie_detail = requests.get(imdb + movie_page)
                source = BeautifulSoup(movie_detail.content, "lxml")
                if source.find("h1", attrs={"class": ""}) == None:

                    movie_name = source.find("h1", attrs={"class": "long"}).text

                else:
                    movie_name = source.find("h1", attrs={"class": ""}).text
                try:
                    duration = source.find("time").text

                except:
                    duration = "No Duration"
                movie_poster_url = source.find("div", attrs={"class": "poster"}).find("img").get("src")
                new_poster_url = ""
                movie_poster_url = movie_poster_url.split(".")
                del movie_poster_url[-2]

                for i in movie_poster_url:
                    new_poster_url += i
                    if movie_poster_url.index(i) < len(movie_poster_url) - 1:
                        new_poster_url += "."

                movie_poster = new_poster_url
                summary = source.find("div", attrs={"class": "summary_text"}).text
                try:
                    movie_rate = source.find("span", attrs={"itemprop": "ratingValue"}).text
                except:
                    movie_rate = "No Rate"
                movie_category = source.find("div", attrs={"class": "subtext"}).find_all("a")


                movie_category_text = ""
                del movie_category[-1]
                for category in movie_category:
                    movie_category_text += category.text + " "



                Movie.objects.create(movie_name=movie_name, poster=movie_poster, imdb_page=imdb + movie_page,
                                     movie_path=path, movie_rate=movie_rate, category=movie_category_text,
                                     duration=duration,summary=summary)



        context = {
            'form': form,
            'user':user,
        }

        return render(request, "movies/add_movie.html", context)
    else:
        return HttpResponse("App is disable")
