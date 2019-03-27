from django import forms
from .models import add_multiple
from .models import Diary





class DiaryForm(forms.ModelForm):


    class Meta:

        model=Diary

        fields=[

            "title",
            "content",
            "date",
        ]

class add_multipleForm(forms.ModelForm):


     class Meta:

         model=add_multiple

         fields=[

             "path",
         ]