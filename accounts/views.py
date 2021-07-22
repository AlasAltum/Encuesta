# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import LoginForm, SignUpForm


def login_view(request):
    """
    Home view with normal url

    """
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == "POST":

        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                msg = "Sucess"
                return render(request, 'accounts/home.html', {"form": form, "msg": msg})

            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, 'landing_page.html', {"form": form, "msg": msg})


def register_view(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=email, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})


def landing_page(request):
    """
    Landing page after login
    """

    if request.user.is_authenticated:
        return render(request, "landing_page.html")

    else:
        return render(request, "not_logged.html")


def logout_from_account(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request, "not_logged.html")

    return render(request, "not_logged.html")


def home(request):
    if request.user.is_authenticated:
        return render(request, "accounts/home.html")

    return render(request, "not_logged.html")



def my_account(request):
    """
    My account page
    """
    if request.user.is_authenticated:
        return render(request, "accounts/my_account.html")

    return render(request, "landing_page.html")