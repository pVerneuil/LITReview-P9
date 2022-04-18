from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


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


class FollowForm(forms.Form):
    user_to_follow = forms.CharField(
        max_length=150,
        label="",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Nom d'utilisateur",
            },
        ),
    )
