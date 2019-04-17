from django.shortcuts import render,HttpResponse

from .models import Book
from home.models import User
from .forms import BookForm,add_multipleForm
import os,magic,webbrowser



def book_index(request):
   books=Book.objects.all()
   user = User.objects.all()
   if user[0].select_book=='E':
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
       len_fav=len(favorite_books)
       len_R=len(bookR)
       len_nR=len(bookNR)
       context={
           "books":books,
           "bookR":bookR,
           "bookNR":bookNR,
           "user": user,
           "fav_book":favorite_books,
           "len_fav":len_fav,
           "len_R":len_R,
           "len_nR":len_nR
        }
       return render(request,"books/book_index.html",context)
   else:
       return HttpResponse("Disable")
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