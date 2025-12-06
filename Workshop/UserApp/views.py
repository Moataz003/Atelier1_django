from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from .forms import CustomUserCreationForm


# ============================
#     REGISTER USER
# ============================
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()     # rôle automatiquement = participant
            messages.success(request, "Votre compte a été créé avec succès !")
            return redirect("login")  # PDF → redirection login
    else:
        form = CustomUserCreationForm()

    return render(request, "register.html", {"form": form})


# ============================
#     LOGIN USER
# ============================
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Bienvenue {user.username} !")
            return redirect("conference_liste")   # Page principale après connexion
    else:
        form = AuthenticationForm()

    return render(request, "login.html", {"form": form})


# ============================
#     LOGOUT USER
# ============================
def logout_view(request):
    logout(request)
    messages.info(request, "Vous êtes déconnecté.")
    return redirect("login")
