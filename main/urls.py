from django.urls import path
from . import views


urlpatterns = [
path('create_ticket', views.create_ticket,name='create_ticket'),
path('', views.home, name = 'home'),
path('response_ticket/<ticket_id>', views.response_ticket, name = 'response_ticket'),
path('ticket_snippet',views.display_ticket,name='ticket')  #!change later
]
