from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import UserFollows


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Nom d'utilisateur"}
        )
        self.fields["password1"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Mot de passe"}
        )
        self.fields["password2"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Confirmer mot de passe"}
        )
        self.fields["password1"].help_text = None
        self.fields["password2"].help_text = None
        self.fields["username"].help_text = None
        self.fields["username"].label = ""
        self.fields["password1"].label = ""
        self.fields["password2"].label = ""


class FollowForm(ModelForm):
    class Meta:
        model = UserFollows
        fields = ["followed_user"]
        labels = {"followed_user": ""}
        widgets = {
            "followed_user": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nom d'utilisateur"}
            ),
        }
