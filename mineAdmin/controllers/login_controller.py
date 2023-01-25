from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def login_user(request):
    try:
        username = request.POST['email']
        pwd = request.POST['pwd']

        user = authenticate(request, username=username, password=pwd)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('index', {'error': 'loginError'}, permanent=True)
    except Exception as e:
        print(e)
        return redirect('index')


def register_user(request):
    email = request.POST['email']
    username = request.POST['username']
    pwd = request.POST['pwd']

    user = User.objects.create_user(username, email, pwd)
    user.save()
    return redirect('index')


def logout_user(request):
    logout(request)
    return redirect('index')
