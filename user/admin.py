from django.contrib import admin
from .models import UserFollows
# Register your models here.


@admin.register(UserFollows)
class Review(admin.ModelAdmin):
    list_display=('user', 'followed_user')
