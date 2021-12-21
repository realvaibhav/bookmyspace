from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from .forms import loginform, signupform

User = get_user_model()
# Create your views here.
def signup_view(request):
    form = signupform(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get("name")
        username = form.cleaned_data.get("username")
        phonenumber = form.cleaned_data.get("phonenumber")
        password = form.cleaned_data.get("password")
        confirm_password = form.cleaned_data.get("confirm_password")
        user = User.objects.create_user(username, password, confirm_password)
        if user != None:
            login(request, user)
            return redirect("/homepage")
        else:
            request.session["signup_error"] = 1
    return render(request, "signup-page.html", {"signup_form" : form})

def login_view(request):
    form = loginform(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)
            return redirect("/homepage")
        else:
            request.session['invalid_user'] = 1
        
    return render(request, "login-page.html", {'login_form': form})

def logout_view(request):
    logout(request)
    return redirect("/login")

def home_view(request):
    return render(request, "customer-homepage.html", {})