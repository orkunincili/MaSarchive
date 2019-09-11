from django.shortcuts import render,HttpResponse

from .models import Book
from home.models import User
from .forms import BookForm,add_multipleForm
import os,magic,webbrowser



def book_index(request):
    user = User.objects.all()
    if user[0].select_movie == 'E':

        if request.POST.get("allbooks") == "allbooks":
            books = Book.objects.all()


        elif request.POST.get("read") == "read":

            books = Book.objects.filter(read="R")


        elif request.POST.get("not read") == "not read":
            books = Book.objects.filter(read="nR")


        elif request.POST.get("reading") == "reading":
            books = Book.objects.filter(read='Rg')


        else:
            books = Book.objects.all()

        len_all = len(Book.objects.all())

        len_rg = len(Book.objects.filter(read="Rg"))

        len_r = len(Book.objects.filter(read="R"))

        len_nr = len(Book.objects.filter(read="nR"))
        context = {
            "books": books,
            "user": user,
            "len_all":len_all,
            "len_rg":len_rg,
            "len_r":len_r,
            "len_nr":len_nr,

        }

        return render(request, "books/book_index.html", context)
    else:
        return HttpResponse("App is disable")

def book_create(request):

    user = User.objects.all()
    if user[0].select_book == 'E':
        form = BookForm(request.POST or None)
        if form.is_valid():
            book = form.save(commit=False)

            book.save()



        context = {
            'form': form,
            'user': user,
        }

        return render(request, "books/book_form.html", context)
    else:
        return HttpResponse("App is disable")

def book_update(request,id):
    book=Book.Objects.get(id=id)
    return HttpResponse("update")


def book_delete(request):
    return HttpResponse("delete")

def book_detail(request,id):
    user = User.objects.all()
    if user[0].select_book == 'E':
        book = Book.objects.get(id=id)
        user = User.objects.all()
        webbrowser.open(book.book_path)
        context = {
            "bookD": book,
            "user": user,
        }

        return render(request, "books/book_detail.html", context)



        return render(request,"books/book_index.html")
    else:
        return HttpResponse("App is disable")
def add_multiple_book(request):
    user = User.objects.all()
    if user[0].select_book == 'E':
        form = add_multipleForm(request.POST or None,request.FILES or None)
        user = User.objects.all()
        file_list=[]
        book_list = []
        if form.is_valid():
            path = form.save()

            for root, dirs, files in os.walk(path.path):
                for file in files:
                    file_list.append(os.sep.join([root, file]))

            for i in range(len(file_list)):

                mime_type = magic.from_file(file_list[i], mime=True)

                if mime_type.lower().endswith(('/pdf', '/epub+zip')) == True:
                    book_list.append(file_list[i].split("/")[-1])

            for i in book_list:


                Book.objects.create(book_name=i,book_path="file://"+path.path+"/"+i)






        context = {
            'form': form,
            'user': user,
        }

        return render(request, "books/add_multiple_book.html", context)
    else:
        return HttpResponse("App is disable")