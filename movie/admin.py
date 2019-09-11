from django.contrib import admin
from .models import Movie








class MovieAdmin(admin.ModelAdmin):
    list_display = ["movie_name", "date"]
    list_filter = ["date"]



admin.site.register(Movie, MovieAdmin)

