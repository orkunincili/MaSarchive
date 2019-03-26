from django import forms
from .models import Book,add_multiple






class BookForm(forms.ModelForm):



    class Meta:

        model=Book

        fields=[

            "book_name",
            "author_name",
            "notes",
            "read",
            "favorite_book",
            "book",
        ]


class add_multipleForm(forms.ModelForm):
    class Meta:
        model = add_multiple

        fields = [

            "path",
        ]