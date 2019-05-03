from django.shortcuts import render
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import Tv,Tv_Series
from home.models import User
from .forms import Tv_SeriesForm,add_multipleForm,TvForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os,magic,webbrowser
from bs4 import BeautifulSoup
import requests,re
global process
import subprocess


# Create your views here.
def tv_index(request):
    tv=Tv_Series.objects.all()
    user=User.objects.all()

    context={
        "tv":tv,
        "user":user,



    }

    return render(request, "tv_series/tv_index.html", context)


def tv_create(request):
    user = User.objects.all()
    if user[0].select_movie == 'E':

        form = Tv_SeriesForm(request.POST or None)


        if form.is_valid():
                tv=form.save(commit=False)
                base_url = 'http://www.imdb.com/find'
                imdb = 'http://www.imdb.com'
                params = dict(q=tv.tv_name, s="tt",ref_="fn_tt")
                r = requests.get(base_url, params=params)
                source = BeautifulSoup(r.content, "lxml")
                tv_page = source.find("td", attrs={"class": "result_text"}).find("a").get("href")
                r = requests.get(imdb + tv_page)
                source = BeautifulSoup(r.content, "lxml")

                if source.find("h1", attrs={"class": ""}) == None:

                    tv_name = source.find("h1", attrs={"class": "long"}).text

                else:
                    tv_name = source.find("h1", attrs={"class": ""}).text
                try:
                    duration = source.find("time").text

                except:
                    duration = "No Duration"
                tv_poster_url = source.find("div", attrs={"class": "poster"}).find("img").get("src")
                new_poster_url = ""
                tv_poster_url = tv_poster_url.split(".")
                del tv_poster_url[-2]

                for i in tv_poster_url:
                    new_poster_url += i
                    if tv_poster_url.index(i) < len(tv_poster_url) - 1:
                        new_poster_url += "."

                tv_poster = new_poster_url
                try:
                    tv_rate = source.find("span", attrs={"itemprop": "ratingValue"}).text
                except:
                    tv_rate = "No Rate"
                tv_category = source.find("div", attrs={"class": "subtext"}).find_all("a")
                tv_category_text = ""
                del tv_category[-1]
                for category in tv_category:
                    tv_category_text += category.text + " "
                seasons = source.find("div", attrs={"class": "seasons-and-year-nav"}).find("a")
                seasons_number=int(seasons.text)
                summary=source.find("div",attrs={"class":"summary_text"}).text
                tv_serie=Tv_Series.objects.create(tv_name=tv_name, tv_poster=tv_poster,
                                     imdb_page=imdb + tv_page,
                                     tv_rate=tv_rate, tv_category=tv_category_text, tv_duration=duration,
                                     seasons_number=seasons_number,summary=summary)


                for s in range(1, int(seasons.text) + 1):
                    r = requests.get(imdb + tv_page + "episodes?season=" + str(s))
                    source = BeautifulSoup(r.content, "lxml")
                    ep_name = source.find("div", attrs={"class": "list detail eplist"})

                    for i in ep_name:

                        try:
                            if i.find("strong").find("a").get("title") != None:
                                episode_name = i.find("strong").find("a").get("title")
                                episode = i.find("div", attrs={"class": ""}).text
                                episode_poster=i.find("img",attrs={"zero-z-index"}).get("src")
                                tv_rate = i.find("span", attrs={"class": "ipl-rating-star__rating"}).text
                                summary = i.find("div", attrs={"class": "item_description"}).text
                                Tv.objects.create(tv_name=tv_serie,season_episode=episode,episode_name=episode_name,
                                                  imdb_page=imdb + tv_page,
                                                  tv_rate=tv_rate, summary=summary,season=s,poster=episode_poster)

                        except:
                            pass

        context = {
            'form': form,
            'user': user,
        }

        return render(request, "tv_series/tv_form.html", context)

    else:
        return HttpResponse("App is disable")


def tv_detail(request,id):
    user = User.objects.all()
    if user[0].select_movie == 'E':
        tv = Tv_Series.objects.get(id=id)






        context = {
            "tvD": tv,
            "user": user,
            "season":range(1,tv.seasons_number+1),


        }

        return render(request, "tv_series/tv_detail.html", context)
    else:
        return HttpResponse("App is disable")

def watch(request,id,id2):
    tv=Tv_Series.objects.get(id=id)
    episode=tv.episodes.get(id=id2)




    context={
       "tv":tv,
       "episode":episode,


    }

    return render(request, "tv_series/watch.html",context )

def add_multiple_tv(request):
        which_tv=TvForm(request.POST or None)
        form = add_multipleForm(request.POST or None)

        if form.is_valid() and which_tv.is_valid():
            which_tv=which_tv.save(commit=False)
            path=form.save()
            movies = os.listdir(path.path)
            movie = []
            for i in movies:
                mime_type = magic.from_file(path.path + i, mime=True)

                if mime_type.startswith("video") == True:
                    movie.append(i)

            new_movie = []
            for i in movie:
                i = i.lower()
                new_movie.append(i)
            new_movie2 = []
            for i in new_movie:
                a = re.findall("s[0-9]*[0-9]+e[0-9]*[0-9]", i)

                a[0] = a[0].replace("s", "S").replace("e", "E")
                a = list(a[0])
                if int(a[1]) == 0:
                    a.remove(a[1])
                    if int(a[3]) == 0:
                        a.remove(a[3])
                else:

                    if int(a[a.index("E") + 1]) == 0 and (a.index("E") + 1) == len(a) - 2:
                        a.remove(a[a.index("E") + 1])

                a.insert(a.index("E"), ",")
                a.insert(a.index("E") + 1, "p")
                a.insert(a.index(",") + 1, " ")
                a.insert(0, "\n\n")
                a.insert(len(a) + 1, "\n")

                episode = ""
                for i in a:
                    episode += i

                new_movie2.append(episode)

            for i in range(len(new_movie2)):
                 tv_name=which_tv.tv_name
                 tv=Tv_Series.objects.get(tv_name=tv_name)

                 tv_episode=tv.episodes.get(season_episode=new_movie2[i])

                 tv_episode.tv_path=path.path+movie[i]
                 tv_episode.save()



        context = {
            "which_tv":which_tv,
            "form": form,

        }
        return render(request, "tv_series/add_tv.html", context)