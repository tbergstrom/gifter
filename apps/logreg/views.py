from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages


def index(request):
    return render(request, "logreg/index.html")


def register(request):
    results = User.objects.validate_register(request.POST)
    if results[0] is False:
        for register_message in results[1]:
            messages.add_message(request, messages.INFO, register_message)
        return redirect('/')
    else:
        return create_session(request, results[1])


def login(request):
    results = User.objects.validate_login(request.POST)
    if results[0] is False:
        print("at login view, false")
        messages.add_message(request, messages.INFO, results[1])
        return redirect('/')
    else:
        return create_session(request, results[1])


def create_session(request, results):
    user = results
    request.session['user'] = {
        "id": user.id,
        "first_name": user.first_name,
        "username": user.username
    }
    return redirect('wishlist:dashboard')


def logout(request):
    request.session.flush()
    return redirect('/')