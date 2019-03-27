from django.shortcuts import render
from .models import Diary
from home.models import User
from .forms import add_multipleForm,DiaryForm
import os,magic,webbrowser



def book_index(request):
   diary=Diary.objects.all()
   user = User.objects.all()

   context={
       "diary":diary,
       "user":user,
   }
   return render(request,"blog/blog_index.html",context)
def book_create(request):
    form = DiaryForm(request.POST or None)
    user = User.objects.all()
    if form.is_valid():
        diary = form.save(commit=False)

        diary.save()



    context = {
        'form': form,
        'user': user,
    }

    return render(request, "blog/blog_form.html", context)


def book_update(request,id):
    book=Diary.Objects.get(id=id)
    return HttpResponse("update")


def book_delete(request):
    return HttpResponse("delete")

def book_detail(request,id):
    diary = Diary.objects.get(id=id)
    user = User.objects.all()

    context = {
        "diaryD": diary,
        "user": user,
    }

    return render(request, "blog/blog_detail.html", context)



    return render(request,"blog/blog_index.html")

