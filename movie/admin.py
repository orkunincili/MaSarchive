from django.contrib import admin
from .models import Movie








class MovieAdmin(admin.ModelAdmin):
    list_display = ["movie_name", "date","category"]
    list_filter = ["date"]
    list_editable = ["category"]


admin.site.register(Movie, MovieAdmin)

