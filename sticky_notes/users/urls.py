from django.urls import path
from . import views

urlpatters = [
    path("signup/", views.signup_view, name="signup")
]
