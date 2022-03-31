from pyexpat import model
from django import forms
from django.forms import ModelForm
from .models import Ticket

class TicketCreationForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ('title', 'description', 'image')
        