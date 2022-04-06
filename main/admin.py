from django.contrib import admin
from .models import Ticket, Review


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("title", "id", "user")


@admin.register(Review)
class Review(admin.ModelAdmin):
    list_display = ("ticket", "id", "user")
