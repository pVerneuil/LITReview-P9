from django.shortcuts import render, redirect
from .forms import TicketCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'main/home.html',{})
@login_required
def create_ticket(request):
    submitted = False
    if request.method == 'POST':
        form = TicketCreationForm(request.POST)
        if form.is_valid():
            new_ticket =form.save(commit= False)
            new_ticket.user = request.user
            new_ticket.save()
            messages.success(request,("Création du ticket réussi"))
            return redirect('/create_ticket?submitted=True')
    else:
        form = TicketCreationForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'main/create_ticket.html',{'form' : form,'submitted': submitted})