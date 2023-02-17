from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse

from django.contrib.auth import authenticate, login, logout
# Create your views here.
def landing(request):
    if request.user.is_authenticated:
        return redirect("app:home")
    return render(request, 'app/landing.html', {})

def home(request):
    if not request.user.is_authenticated:
        return redirect("account:login")
    return render(request, 'app/home.html', {})


def track(request):
    if not request.user.is_authenticated:
        return redirect("account:login")
    return render(request, 'app/track.html', {})


def contact(request):
    if not request.user.is_authenticated:
        return redirect("account:login")
    return render(request, 'app/contact.html', {})
