from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)  # Instantiate the form with the submitted data
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request,
                username=cd["username"],
                password=cd["password"],
            )
            if user is not None:
                if user.is_active:
                    login(request, user)  # persists and sets user current session
                    return HttpResponse("Authenticated " "successfully")
                else:
                    return HttpResponse("Disabled account")
            else:
                return HttpResponse("Invalid login")
    else:
        form = LoginForm()

    return render(request, "account/login.html", {"form": form})


# checks whether the current user is authenticated
# If the user is authenticated, it executes the decorated view; 
# if the user is not authenticated, it redirects the user to 
# the login URL with the originally requested URL as a GET parameter named next.
@login_required
def dashboard(request):
    return render(
        request,
        "account/dashboard.html",
        {"section": "dashboard"},
    )


