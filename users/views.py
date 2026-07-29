from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib import messages


def login_view(request):

    #Initializes both login & register forms
    login_form = AuthenticationForm()
    reg_form = CustomUserCreationForm()

    #Tracks which box to show (login by default)
    show_reg = False

    if request.method == "POST":

        #Registeration logic
        if "register_btn" in request.POST:
            reg_form = CustomUserCreationForm(request.POST)

            #Validates registration form
            if reg_form.is_valid():
                reg_form.save()
                messages.success(request, "Account created successfully! Please login.")
                return redirect("login")

            else:
                #If registration fails, returns form with errors and shows register box
                return render(request, "login.html", {
                    "reg_form": reg_form,
                    "show_reg": True,
                    "error": "Registration failed. Please fix the errors below."
                })

        #Login logic
        u_name = request.POST.get("username")
        p_word = request.POST.get("password")

        #Authenticate user credentials
        user = authenticate(request, username=u_name, password=p_word)

        if user is not None:
            login(request, user)

            #Redirect staff users to Django admin panel
            if user.is_staff:
                return redirect('/admin/')

            #Redirect normal users to dashboard
            return redirect("dashboard")

        else:
            #If login fails, shows error message
            return render(request, "login.html", {
                "error": "Invalid username or password",
                "reg_form": reg_form
            })

    #Default GET request (load login page)
    return render(request, "login.html", {"reg_form": reg_form})


@login_required
def dashboard(request):
    #Renders dashboard page after successful login
    return render(request, "index.html")


def logout_view(request):
    #Logs out user and clears session
    logout(request)

    #Redirects back to login page
    return redirect("login")