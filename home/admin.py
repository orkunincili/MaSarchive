from django.contrib import admin


from home.models import User

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ["user_name"]


admin.site.register(User,UserAdmin)


