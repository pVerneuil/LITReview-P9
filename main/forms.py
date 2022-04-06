from django import forms
from django.forms import ModelForm
from .models import Ticket, Review

class TicketCreationForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ('title', 'description', 'image')
        labels = {
            'title': 'Titre',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class' :'form-control'}),
            'image':forms.FileInput(attrs={'class' :'form-control','buttonText':"Your label here."}),
        }

class ReviewResponseForm(ModelForm):
    class Meta:
        model = Review
        fields = ('headline', 'rating', 'body')
        labels = {
            'headline' : 'Titre',
            'rating' : 'Note',
            'body' : 'Commentaire'
        }
        CHOICES = [
            ('0', ' 0'), ('1', ' 1'), ('2', ' 2'),
            ('3', ' 3'), ('4', ' 4'), ('5', ' 5')]
        widgets = {
                'headline': forms.TextInput(attrs={'class':'form-control'}),
                'body': forms.Textarea(attrs={'class':'form-control'}), 
                'rating' : forms.RadioSelect(choices= CHOICES, attrs={}),
            
        }

