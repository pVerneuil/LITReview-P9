from django.shortcuts import render, redirect
from .forms import TicketCreationForm, ReviewResponseForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Ticket, Review
from user.models import UserFollows
from django.contrib.auth.models import User
from itertools import chain
from django.db.models import CharField, Value
from django.shortcuts import render


def get_user_viewable_content(current_user):
    users_followed_by_current_user = [
        user.followed_user for user in UserFollows.objects.filter(user=current_user)
    ]
    users_to_display_content_from = users_followed_by_current_user + [current_user]
    viewable_reviews = Review.objects.filter(user__in=users_to_display_content_from)
    viewable_ticket = Ticket.objects.filter(user__in=users_to_display_content_from)
    return viewable_reviews, viewable_ticket


@login_required
def home(request):
    reviews, tickets = get_user_viewable_content(request.user)
    reviews = reviews.annotate(content_type=Value("REVIEW", CharField()))
    tickets = tickets.annotate(content_type=Value("TICKET", CharField()))
    posts = sorted(
        chain(reviews, tickets), key=lambda post: post.time_created, reverse=True
    )
    return render(
        request,
        "main/home.html",
        {
            "posts": posts,
            "display_review_button": True,
        },
    )


@login_required
def see_my_posts(request):
    my_tickets = Ticket.objects.filter(user=request.user)
    my_tickets = my_tickets.annotate(content_type=Value("TICKET", CharField()))

    my_reviews = Review.objects.filter(user=request.user)
    my_reviews = my_reviews.annotate(content_type=Value("REVIEW", CharField()))

    my_posts = sorted(
        chain(my_reviews, my_tickets), key=lambda post: post.time_created, reverse=True
    )
    return render(
        request,
        "main/my_posts.html",
        {
            "my_posts": my_posts,
            "display_modify_delete_buttons": True,
        },
    )


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
    ticket = Ticket.objects.get(pk=ticket_id)
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


@login_required
def delete_content(request, content_id, content_type):
    if content_type == "ticket":
        post = Ticket.objects.get(pk=content_id)
    elif content_type == "review":
        post = Review.objects.get(pk=content_id)
    post.delete()
    messages.success(request, ("Élément supprimé avec succès"))
    return redirect("my_posts")


@login_required
def update_ticket(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    form = TicketCreationForm(
        request.POST or None, request.FILES or None, instance=ticket
    )
    if form.is_valid():
        form.save()
        messages.success(request, ("Ticket modifié avec succès"))
        return redirect("my_posts")
    return render(
        request,
        "main/update_ticket.html",
        {
            "ticket": ticket,
            "form": form,
        },
    )


@login_required
def update_review(request, review_id):
    review = Review.objects.get(pk=review_id)
    form = ReviewResponseForm(request.POST or None, instance=review)
    if form.is_valid():
        form.save()
        messages.success(request, ("Critque modifiée avec succès"))
        return redirect("my_posts")
    return render(
        request,
        "main/update_review.html",
        {
            "review": review,
            "ticket": review.ticket,
            "form": form,
        },
    )
