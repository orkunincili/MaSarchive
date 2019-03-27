from django import forms
from .models import Movie,add_multiple

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie

        fields = [

            "movie_name",
            "notes",
            "watch",
            "movie",
            "favorite_movie",
            "movie_path",
        ]


class add_multipleForm(forms.ModelForm):
    class Meta:
        model = add_multiple

        fields = [

            "path",
        ]