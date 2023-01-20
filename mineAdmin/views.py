from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, 'views/index.html')


def play(request):
    return render(request, 'views/play.html')


def stats(request):
    return render(request, 'views/stats.html')


def tools(request):
    return render(request, 'views/tools.html')


def login_user(request):
    username = request.POST['username']
    pwd = request.POST['pwd']

    user = authenticate(request, username=username, password=pwd)
    if user is not None:
        login(request, user)
        return redirect('index')
    else:
        return redirect('index')


def register_user(request):
    username = request.POST['username']
    pwd = request.POST['pwd']

    user = User.objects.create_user(username, 'prueba@prueba', pwd)
    user.save()
    return redirect('index')


def logout_user(request):
    logout(request)
    return redirect('index')
