from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    """
    Form for user signup.
    
    Fields:
        - username: Charfield, uses bootstrap text input.
        - email: Charfield, uses bootstrap email input.
        - password1: Charfield, uses bootstrap password input.
        - password2: Charfield, uses bootstrap password input.
        """
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control"}),
        }


class LoginForm(AuthenticationForm):
    """
    User login form.

    Fields:
        - username: Charfield, uses bootstrap text input.
        - password: Charfield, uses bootstrap password input.
    """
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}))
