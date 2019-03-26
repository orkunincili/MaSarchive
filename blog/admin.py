from django.contrib import admin
from blog.models import add_multiple

# Register your models here.



class add_multipleAdmin(admin.ModelAdmin):
    list_display = ["path"]


admin.site.register(add_multiple,add_multipleAdmin)
