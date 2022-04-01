from django.urls import path
from . import views


urlpatterns = [
path('create_ticket', views.create_ticket,name='create_ticket'),
path('', views.home, name = 'home'),
path('ticket_snippet',views.display_ticket,name='ticket')  #!change later
]
