from django.contrib import admin
from blog.models import Diary

# Register your models here.



class DiaryAdmin(admin.ModelAdmin):
    list_display = ["title","content"]


admin.site.register(Diary,DiaryAdmin)
