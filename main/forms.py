from cProfile import label
from pyexpat import model
from django import forms
from django.forms import ModelForm
from .models import Ticket

class TicketCreationForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ('title', 'description', 'image')

        labels = {
            'title': 'Titre',
        }
        
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','title': 'Your name'}),
            'description':forms.Textarea(attrs={'class' :'form-control'}),
            'image':forms.FileInput(attrs={'class' :'form-control','buttonText':"Your label here."}),
        }
        