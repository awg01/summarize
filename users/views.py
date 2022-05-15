from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserRegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.views.generic.list import ListView
from django.urls import reverse
from multi_form_view import MultiModelFormView
from django.utils.crypto import get_random_string
from . models import *


def handle_server_error(request, exception=None):
    return render(request, "users/not_found.html")

def handle_page_not_found(request, exception=None):
    return render(request, "users/not_found.html")

def home(request):
    return render(request, "users/home.html")

@login_required
def profile(request):
    return render(request, "users/profile.html")

@login_required
def dictionary(request):
    return render(request, "users/summary/dictionary.html")

def about_us(request):
    return render(request, "users/about_us.html")

from django.contrib.auth import login, authenticate  # add to imports

def login_page(request):
    print("called loginform")
    form = LoginForm()
    message = ''
    if request.method == 'POST':
        print("inside post")
        form = LoginForm(request.POST)
        if form.is_valid():
           # check user exists
           print("form is valid")
           username=form.cleaned_data['username']
           user_exists = User.objects.filter(username=username).exists()
           print("line 48")
           if not user_exists:
               print("user doesnt exists")
               message = 'Invalid credentials !'
               return redirect("users:login")
           print("user exists   ")

           user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
           # print("line 56")
           # print({user.username})
           # print({user.password})
           if user is not None:
               print({user.username})
               login(request, user)
               print("after login")
               message = f'Hello {user.username}! You have been logged in'
               return redirect("users:home")
           else:
               message = 'Login failed!'
               return redirect("users:login")


    return render(request, 'users/login.html', context={'form': form, 'message': message})

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Hi {username}, your account is created successfully.")
            return redirect("users:home")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form":form})
