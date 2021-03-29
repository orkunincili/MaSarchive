# -*- coding: utf-8 -*-
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import Movie
from home.models import User
from .forms import MovieForm,add_multipleForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os,magic,webbrowser,subprocess,requests,shutil
global process
from .scraping import Scrape








# Create your views here.


def movies(request):


        if request.POST.get("allmovies") == "allmovies":
            movies = Movie.objects.all()


        elif request.POST.get("watched")=="watched":

            movies=Movie.objects.filter(watch="W")


        elif request.POST.get("not watched") == "not watched":
            movies=Movie.objects.filter(watch="nW")


        elif request.POST.get("favorites") == "favorites":
            movies=Movie.objects.filter(favorite_movie='F')

        else:
          movies = Movie.objects.all()


        if request.POST.get("sort by rating") == "sort by rating":
         movies = list(movies)
         no_rate_movies=[]
         for i in movies:
            if i.movie_rate == "No Rate":
                movies.remove(i)
                no_rate_movies.append(i)
         for i in range(len(movies)):
             for j in range(0, len(movies) - i - 1):
                    if movies[j].movie_rate == "No Rate":
                        movies.insert(-1,movies[j])

                    elif float(movies[j].movie_rate) > float(movies[j + 1].movie_rate):
                        movies[j], movies[j + 1] = movies[j + 1], movies[j]
         for x in no_rate_movies:
            movies.insert(0,x)
         movies.reverse()

        paginator = Paginator(movies, 42)

        page = request.GET.get('page')
        try:
            movies = paginator.page(page)
        except PageNotAnInteger:

            movies = paginator.page(1)
        except EmptyPage:

            movies = paginator.page(paginator.num_pages)

        len_all=len(Movie.objects.all())

        len_fav = len(Movie.objects.filter(favorite_movie="F"))

        len_W = len(Movie.objects.filter(watch="W"))

        len_nW = len(Movie.objects.filter(watch="nW"))

        context = {
            "movies":movies,
            "user": user,
            "len_all":len_all,
            "len_fav": len_fav,
            "len_W": len_W,
            "len_nW": len_nW,


        }

        return render(request, "movies/movies.html", context)


def movie_create(request):


        form = MovieForm(request.POST or None)
        user = User.objects.all()
        context = {
            'form': form,
            'user': user,
        }

        if form.is_valid():
                movie=form.save(commit=False)


                result = Scrape().search(movie.movie_name)



                if not Movie.objects.get(movie_name=result['movie_name']):

                    movie = Movie.objects.create(movie_name=result['movie_name'],
                                               poster=result['movie_poster_url'],
                                               watch=movie.watch,
                                               imdb_page=result['imdb_page'],
                                               movie_rate=result['movie_rate'],
                                               category=result['movie_category'],
                                               duration=result['duration'],
                                               summary=result['summary'])


                   return HttpResponseRedirect(movie.get_absolute_url())



        return render(request, "movies/movies_form.html", context)


def movie_update(request,id):


        movie = Movie.objects.get(id=id)
        user = User.objects.all()
        form = MovieForm(request.POST or None, request.FILES or None, instance=movie)
        if form.is_valid():
            form.save()


            return HttpResponseRedirect(movie.get_absolute_url())
        context = {
            'form': form,
            'movie':movie,
        }


        return render(request, "movies/movies_form.html", context)


def movie_detail(request,id):


        movie=Movie.objects.get(id=id)
        user = User.objects.all()
        form = MovieForm(request.POST or None, request.FILES or None, instance=movie)
        if request.POST.get("Play") == 'Play':
            subprocess.call(['vlc',movie.movie_path])
            return HttpResponseRedirect(movie.get_absolute_url())
        if form.is_valid():
            form.save()
            movie.save()
            return HttpResponseRedirect(movie.get_absolute_url())





        context={
            "form":form,
            "movieD":movie,



        }

        return render(request,"movies/movie_detail.html",context)


def add_multiple_movie(request):

    movie_poster = "/home/orkun/PersonalBlog/static/images/movie_poster/"

        form = add_multipleForm(request.POST or None)
        user=User.objects.all()
        file_list=[]
        movie_name_list=[]
        movie_path_list=[]

        if request.POST.get("top250") == "top250":
            


            r = requests.get(base_url)
            source = BeautifulSoup(r.content, "html.parser")
            top250 = source.findAll("div", attrs={"class": "lister-item mode-advanced"})

            for i in top250:
                movie_name=i.find("h3").find("a").text
                movie_page=i.find("h3").find("a").get("href")
                duration=i.find("span", attrs={"class": "runtime"}).text
                movie_rate=i.find("strong").text
                category=i.find("span", attrs={"class": "genre"}).text
                summary = i.findAll("p", attrs={"class": "text-muted"})
                summary = summary[1].text



                movie_poster_url = i.find("img").get("loadlate")
                new_poster_url = ""
                movie_poster_url = movie_poster_url.split(".")
                img_type=movie_poster_url[-1]
                del movie_poster_url[-2]

                for i in movie_poster_url:
                    new_poster_url += i
                    if movie_poster_url.index(i) < len(movie_poster_url) - 1:
                        new_poster_url += "."

                url = new_poster_url
                response = requests.get(url, stream=True)
                with open(movie_poster + "{}.{}".format(movie_name.replace(" ", "-"), img_type), 'wb') as out_file:
                    shutil.copyfileobj(response.raw, out_file)
                del response

                poster = movie_name.replace(" ", "-") + "." + img_type



                movie_exist=0;
                for i in Movie.objects.all():
                   if movie_name==i.movie_name:
                       movie_exist=1
                       break;
                if movie_exist==0:
                    Movie.objects.create(movie_name=movie_name, poster=poster,
                                         imdb_page=imdb + movie_page, movie_rate=movie_rate,
                                         category=category, duration=duration,
                                         summary=summary)
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

                params = dict(q=movie_name_list[i], s="tt", ttype="ft", ref_="fn_ft")


                r = requests.get(base_url, params=params)
                source = BeautifulSoup(r.content, "html.parser")

                if source.find("td", attrs={"class":"result_text"})==None:
                    params = dict(ref_="nv_sr_fn", q=movie_name_list[i], s="tt")
                    r = requests.get(base_url, params=params)
                    source = BeautifulSoup(r.content, "html.parser")
                movie_page = source.find("td", attrs={"class":"result_text"}).find("a").get("href")
                movie_detail = requests.get(imdb + movie_page)
                source = BeautifulSoup(movie_detail.content, "html.parser")
                if source.find("h1", attrs={"class": ""}) == None:

                    movie_name = source.find("h1", attrs={"class": "long"}).text

                else:
                    movie_name = source.find("h1", attrs={"class": ""}).text
                try:
                    duration = source.find("time").text

                except:
                    duration = "No Duration"
                base = "https://www.youtube.com/results?search_query="
                qstring = movie_name + " official trailer"
                re = requests.get(base + qstring)

                page = re.text
                soup = BeautifulSoup(page, 'html.parser')

                movie_trailer = soup.find('a', attrs={'class': 'yt-uix-tile-link'}).get("href")

                movie_trailer = movie_trailer.split("=")
                movie_trailer = "http://www.youtube.com/embed/" + movie_trailer[-1]

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



                Movie.objects.create(movie_name=movie_name, poster=poster, imdb_page=imdb + movie_page,
                                     movie_path=path, movie_rate=movie_rate, category=movie_category_text,
                                     duration=duration,summary=summary,movie_trailer=movie_trailer)



        context = {
            'form': form,

        }

        return render(request, "movies/add_movie.html", context)
