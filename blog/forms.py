from django import forms
from .models import add_multiple








class add_multipleForm(forms.ModelForm):


     class Meta:

         model=add_multiple

         fields=[

             "path",
         ]