# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User


class LoginForm(forms.Form):
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Correo electrónico",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Contraseña",
                "class": "form-control"
            }
        ))


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Correo Electrónico",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Contraseña",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Verificación de contraseña",
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')
