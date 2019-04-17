from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import Diary
from home.models import User
from .forms import DiaryForm
import os,magic,webbrowser



def blog_index(request):
   diary=Diary.objects.all()
   user = User.objects.all()

   context={
       "diary":diary,
       "user":user,
   }
   return render(request,"blog/blog_index.html",context)
def blog_create(request):
    form = DiaryForm(request.POST or None)
    user = User.objects.all()
    if form.is_valid():
        form.save()





    context = {
        'form': form,
        'user': user,
    }

    return render(request, "blog/blog_form.html", context)


def blog_update(request,id):

    user = User.objects.all()
    if user[0].select_movie == 'E':
        post = Diary.objects.get(id=id)
        user = User.objects.all()
        form = DiaryForm(request.POST or None, request.FILES or None, instance=post)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(post.get_absolute_url())
        context = {
            'form': form,
            'user': user,
            'post': post,
        }

        return render(request, "movies/blog_form.html", context)
    else:
        return HttpResponse("App is disable")



def blog_delete(request,id):

    return HttpResponse("delete")

def blog_detail(request,id):
    postD = Diary.objects.get(id=id)
    user = User.objects.all()

    context = {
        "postD": postD,
        "user": user,
    }

    return render(request, "blog/blog_detail.html", context)



    return render(request,"blog/blog_index.html")

