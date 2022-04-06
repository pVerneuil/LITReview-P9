from django.shortcuts import render, redirect
from .forms import TicketCreationForm, ReviewResponseForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Ticket, Review
from django.contrib.auth.models import User


@login_required
def home(request):
    # ticket = Ticket.objects.get(pk = 12)    #! test with one ticket
    review = Review.objects.get(pk=1)  #! test with one review
    ticket = review.ticket
    return render(
        request,
        "main/home.html",
        {
            "review": review,
        },
    )


@login_required
def my_posts(request):
    user = request.user
    return render(request, "main/my_posts.html", {"user": user})


@login_required
def create_ticket(request):
    submitted = False
    if request.method == "POST":
        form = TicketCreationForm(request.POST, request.FILES)
        if form.is_valid():
            new_ticket = form.save(commit=False)
            new_ticket.user = request.user
            new_ticket.save()
            messages.success(request, ("Création du ticket réussi"))
            return redirect("/create_ticket?submitted=True")
    else:
        form = TicketCreationForm
        if "submitted" in request.GET:
            submitted = True
    return render(
        request, "main/create_ticket.html", {"form": form, "submitted": submitted}
    )


@login_required
def response_ticket(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)  #! test with one ticket
    submitted = False
    if request.method == "POST":
        form = ReviewResponseForm(request.POST)
        if form.is_valid():
            new_reveiw = form.save(commit=False)
            new_reveiw.user = request.user
            new_reveiw.ticket = ticket
            new_reveiw.save()
            messages.success(request, ("Création de la critique réussi"))
            return redirect("/my_posts")
    else:
        form = ReviewResponseForm
        if "submitted" in request.GET:
            submitted = True
    return render(
        request,
        "main/response_ticket.html",
        {"ticket": ticket, "form": form, "submitted": submitted},
    )


@login_required
def create_review(request):
    submitted = False
    if request.method == "POST":
        ticket_form = TicketCreationForm(request.POST)
        review_form = ReviewResponseForm(request.POST, request.FILES)

        if ticket_form.is_valid() and review_form.is_valid():
            new_ticket = ticket_form.save(commit=False)
            new_ticket.user = request.user

            new_reveiw = review_form.save(commit=False)
            new_reveiw.user = request.user
            new_reveiw.ticket = new_ticket

            new_ticket.save()
            new_reveiw.save()
            messages.success(request, ("Création de la critique réussi"))
            return redirect("/create_review?submitted=True")
    else:
        ticket_form = TicketCreationForm
        review_form = ReviewResponseForm
        if "submitted" in request.GET:
            submitted = True
    return render(
        request,
        "main/create_review.html",
        {
            "ticket_form": ticket_form,
            "review_form": review_form,
            "submitted": submitted,
        },
    )
