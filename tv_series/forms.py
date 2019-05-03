from django import forms
from .models import Tv_Series,add_multiple,Tv

class Tv_SeriesForm(forms.ModelForm):
    class Meta:
        model = Tv_Series

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

        fields = [

            "path",
        ]