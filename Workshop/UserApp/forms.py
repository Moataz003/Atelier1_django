from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        # On n'affiche JAMAIS "role" ici (PDF partie 2)
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "affiliation",
            "nationality",
        )

        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "affiliation": forms.TextInput(attrs={"class": "form-control"}),
            "nationality": forms.TextInput(attrs={"class": "form-control"}),
        }

    def save(self, commit=True):
        # On appelle la logique standard pour créer l'utilisateur
        user = super().save(commit=False)

        # Le PDF impose que le rôle = participant automatiquement
        user.role = "participant"

        if commit:
            user.save()

        return user
