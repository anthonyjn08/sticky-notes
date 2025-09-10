from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignupForm


# Create your views here.
def signup_view(request):
    """
    Displays a signup form allowing new users to sign up.
    """
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect("note_list")
    else:
        form = SignupForm()

    return render(request, "signup.html", {"form": form})
