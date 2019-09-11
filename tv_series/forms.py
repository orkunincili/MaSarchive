from django import forms
from .models import Tv_Series,add_multiple,Tv

class Tv_SeriesForm(forms.ModelForm):
    class Meta:
        model = Tv_Series
        widgets = {
            'tv_name': forms.TextInput(attrs={'placeholder': 'e.g. Rick and Morty'}),

        }

        fields = [

            "tv_name",



        ]
class TvForm(forms.ModelForm):
    class Meta:
        model=Tv

        fields={
            "tv_name",
        }


class add_multipleForm(forms.ModelForm):
    class Meta:
        model = add_multiple
        widgets = {
            'path': forms.TextInput(attrs={'placeholder': '/path/to/tv/show/episodes/'}),

        }

        fields = [

            "path",
        ]