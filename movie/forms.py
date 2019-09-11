# -*- coding: utf-8 -*-
from django import forms
from .models import Movie,add_multiple

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        widgets = {
            'movie_name': forms.TextInput(attrs={'placeholder': 'movie name'}),
            'movie_path': forms.TextInput(attrs={'placeholder': '/path/to/movie/movie_name (if you have)'}),

        }

        fields = [

            "movie_name",
            "notes",
            "watch",
            "favorite_movie",
            "movie_path",
            "summary",


        ]


class add_multipleForm(forms.ModelForm):
    class Meta:
        model = add_multiple
        widgets = {
            'path': forms.TextInput(attrs={'placeholder': '/path/to/your/movies'}),
        }

        fields = [

            "path",
        ]
