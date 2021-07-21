# Create your views here.
from django.contrib.auth import authenticate, login
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
                return HttpResponseRedirect('landing_page/')

            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, 'accounts/login.html', {"form": form, "msg": msg})


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
    msg = None
    success = False

    if request.user.is_authenticated:
        # Do something for authenticated users.
        return render(request, "landing_page.html", {"msg": msg, "success": success})

    else:
        return render(request, "not_logged.html", {"msg": msg, "success": success})
