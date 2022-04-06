from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterUserForm, FollowForm
from django.contrib.auth.models import User
from .models import UserFollows

def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.warning(request, ("Nom d'utilisateur ou mot de passe invalide. Veuiller réessayer"))	
			return redirect('login')	


	else:
		return render(request, 'authenticate/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, ("Déconnexion réussie"))
    return redirect('login')

def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password= password)
            login(request, user)
            messages.success(request,("Inscription réussi"))
            return redirect('home')
    else:
        form = RegisterUserForm()
    return render(request, 'authenticate/register_user.html',{
		'form' : form
	})
    
@login_required
def follows(request):
    submitted = False
    if request.method == 'POST':
        form = FollowForm(request.POST)
        print(form)
        if form.is_valid(): #! does validate
            new_follow = form.save(commit= False)
            new_follow.user = request.user
            new_follow.save()
            messages.success(request,("Abonnement réussi"))
            return redirect('/follows?submitted=True')
        
    else:
        form = FollowForm
        if 'submitted' in request.GET:
            submitted = True
    followed_by = UserFollows.objects.filter(user = request.user)
    following = UserFollows.objects.filter(followed_user = request.user)
    return render(request, 'follows/follows.html',
                {'form' : form,
                'submitted': submitted,
                'following': following,
                'followed_by' : followed_by,
                })


@login_required
def unfollow(request, follow_id):
    subs = UserFollows.objects.get(pk=follow_id)
    subs.delete()
    return redirect('follows')