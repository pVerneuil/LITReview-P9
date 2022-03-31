from django.shortcuts import render, redirect
from .forms import TicketCreationForm
from django.contrib import messages


def home(request):
    return render(request, 'main/home.html',{})

def create_ticket(request):
    submitted = False
    if request.method == 'POST':
        form = TicketCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,("Création du ticket réussi"))
            return redirect('/create_ticket?submitted=True')
    else:
        form = TicketCreationForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'main/create_ticket.html',{'form' : form,'submitted': submitted})