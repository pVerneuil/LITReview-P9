from django.urls import path
from . import views


urlpatterns = [
path('', views.home, name = 'home'),
path('create_ticket', views.create_ticket,name='create_ticket'),
]
