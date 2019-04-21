from django.contrib import admin
from .models import Tv_Series,Tv
# Register your models here.
class Tv_SeriesAdmin(admin.ModelAdmin):
    list_display = ["tv_name"]




admin.site.register(Tv_Series, Tv_SeriesAdmin)


class TvAdmin(admin.ModelAdmin):
    list_display = ["tv_name","season_episode","episode_name"]



admin.site.register(Tv, TvAdmin)

