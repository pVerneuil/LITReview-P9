from django.contrib import admin
from .models import Ticket
from .models import Review
from .models import UserFollows

admin.site.register(Ticket)
admin.site.register(Review)
admin.site.register(UserFollows)