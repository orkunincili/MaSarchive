from django.shortcuts import render

from .models import Book
from home.models import User
from .forms import BookForm,add_multipleForm
import os,magic,webbrowser



def book_index(request):
   books=Book.objects.all()
   user = User.objects.all()
   bookR=[]
   bookNR=[]
   favorite_books=[]
   for i in books:
       if(i.favorite_book=="F"):
           favorite_books.append(i)
       elif(i.read=='R'):
           bookR.append(i)
       else:
           bookNR.append(i)
   context={

       "bookR":bookR,

       "bookNR":bookNR,

       "user": user,

       "fav_book":favorite_books,
    }
   return render(request,"books/book_index.html",context)
def book_create(request):
    form = BookForm(request.POST or None)
    user = User.objects.all()
    if form.is_valid():
        book = form.save(commit=False)

        book.save()



    context = {
        'form': form,
        'user': user,
    }

    return render(request, "books/book_form.html", context)


def book_update(request,id):
    book=Book.Objects.get(id=id)
    return HttpResponse("update")


def book_delete(request):
    return HttpResponse("delete")

def book_detail(request,id):
    book = Book.objects.get(id=id)
    user = User.objects.all()
    webbrowser.open(book.book_path)
    context = {
        "bookD": book,
        "user": user,
    }

    return render(request, "books/book_detail.html", context)



    return render(request,"books/book_index.html")

def add_multiple_book(request):
    form = add_multipleForm(request.POST or None,request.FILES or None)
    user = User.objects.all()
    books_list = []
    if form.is_valid():
        books_path = form.save()

        books = os.listdir(books_path.path)

        for i in books:

            b = magic.from_file(books_path.path + i, mime=True)
            if b.lower().endswith(('/pdf', '/epub+zip')) == True:
                books_list.append(i)

        for i in books_list:


            Book.objects.create(book_name=i,book_path="file://"+books_path.path+i)



    context = {
        'form': form,
        'user': user,
    }

    return render(request, "books/add_multiple_book.html", context)