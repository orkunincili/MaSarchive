from bs4 import BeautifulSoup
import requests,shutil
global process
import subprocess



class Scrape():

    base_url = 'http://www.imdb.com/find'
    top250_url = 'https://www.imdb.com/search/title?title_type=feature&sort=num_votes,desc&count=250'
    base_url_top250
    imdb_url = 'http://www.imdb.com'
    ref="nv_sr_fn"
    s="tt"
    movie_page=""
    #params = dict(ref_="nv_sr_fn", q=self.movie_name, s="tt")


    def get_infos(self, path):

        movie_detail = requests.get(self.imdb_url + path)
        source = BeautifulSoup(movie_detail.content, "html.parser")
        if source.find("h1", attrs={"class": ""}) == None:

            movie_name = source.find("h1", attrs={"class": "long"}).text

        else:
            movie_name = source.find("h1", attrs={"class": ""}).text

        try:
            duration = source.find("time").text

        except:
            duration = "No Duration"

        movie_poster_url = source.find("div", attrs={"class": "poster"}).find("img").get("src")

        edited_poster_url = self.fix_poster_url(movie_poster_url)


        try:
           movie_rate = source.find("span", attrs={"itemprop": "ratingValue"}).text
        except:
           movie_rate="No Rate"

        summary = source.find("div", attrs={"class": "summary_text"}).text
        movie_category = source.find("div", attrs={"class": "subtext"}).find_all("a")


        movie_category_text = ""
        del movie_category[-1]
        for category in movie_category:
            movie_category_text+=category.text+" "

        result = dict(movie_name=movie_name,
                      duration=duration,
                      movie_poster_url=edited_poster_url,
                      movie_rate=movie_rate,
                      summary=summary,
                      movie_category=movie_category_text,
                      imdb_page=self.movie_page)

        return result


    def create_imdb_page(self, path):

        self.movie_page = self.imdb_url+path

    def fix_poster_url(self, url):

        new_poster_url = ""
        movie_poster_url = url.split(".")

        del movie_poster_url[-2]

        for i in movie_poster_url:
            new_poster_url += i
            if movie_poster_url.index(i) < len(movie_poster_url) - 1:
                new_poster_url += "."

        return new_poster_url

    def get_page(self, path):

        r = requests.get(self.imdb_url + path)
        source = BeautifulSoup(r.content, "html.parser")
        movie_page_path = source.find("td", attrs={"class": "result_text"}).find("a").get("href")

        self.create_imdb_page(movie_page_path)

        return self.get_infos(movie_page_path)


    def search(self, movie_name):
        params = dict(ref_=self.ref, q=movie_name, s=self.s)
        r = requests.get(self.base_url, params=params)
        source = BeautifulSoup(r.content, "html.parser")
        search_path = source.find("ul", attrs={"class": "findTitleSubfilterList"}).find("a").get("href")

        return self.get_page(search_path)
