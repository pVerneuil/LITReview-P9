from django.shortcuts import render, redirect
from .forms import TicketCreationForm, ReviewResponseForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Ticket, Review
from django.contrib.auth.models import User

@login_required
def home(request):
    ticket = Ticket.objects.get(pk = 12) #! test with one ticket
    return render(request, 'main/home.html',{
        "ticket": ticket ,
    })
@login_required
def create_ticket(request):
    submitted = False
    if request.method == 'POST':
        form = TicketCreationForm(request.POST, request.FILES)
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

def display_ticket(request): #!do i need that?
    ticket = Ticket.objects.filter(user = request.user)  
    return render(request, 'main/ticket_snippet.html', {
			"ticket": ticket ,
			})
    
@login_required
def response_ticket(request,ticket_id):
    ticket = Ticket.objects.get(pk = ticket_id) #! test with one ticket
    submitted = False
    if request.method == 'POST':
        form = ReviewResponseForm(request.POST)
        if form.is_valid():
            new_reveiw =form.save(commit= False)
            new_reveiw.user = request.user
            new_reveiw.ticket = ticket
            new_reveiw.save()
            messages.success(request,("Création de la critique réussi"))
            return redirect('/response_ticket?submitted=True')
    else:
        form = ReviewResponseForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'main/response_ticket.html',{
        "ticket": ticket,
        'form' : form,
        'submitted': submitted})
