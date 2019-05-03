from django import forms
from .models import User



class UserForm(forms.ModelForm):



    class Meta:

        model=User


        fields=[
            'user_name',
            'movie',
            'select_movie',
            'blog',
            'select_blog',
            'book',
            'select_book',
            'tv_series',
            'select_tv',


        ]


