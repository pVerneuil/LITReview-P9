from .models import UserFollows
from django.contrib import admin
from django.contrib.auth.models import User


class MyUserAdmin(admin.ModelAdmin):
    list_display = ["username", "id"]


admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)

# Register your models here.


@admin.register(UserFollows)
class UserFollos(admin.ModelAdmin):
    list_display = ("user", "followed_user")
