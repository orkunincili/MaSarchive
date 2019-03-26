from django import forms
from .models import User



class UserForm(forms.ModelForm):



    class Meta:

        model=User


        fields=[
            'user_name',
            'tv_series',
            'movie',
            'blog',
            'book',

        ]


