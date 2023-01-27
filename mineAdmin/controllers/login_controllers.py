from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def index(request):
    if request.method == 'GET':
        login_form = AuthenticationForm(None)
        register_form = UserCreationForm(None)
        return render(request, 'views/index.html', {'login_form': login_form, 'register_form': register_form})

    elif request.method == 'POST':
        if 'login-button' in request.POST:
            login_form = AuthenticationForm(request.POST)
            if not login_form.is_valid():
                return render(request, "views/index.html",
                              {'login_form': login_form, 'register_form': UserCreationForm(None)})



        elif 'register-button' in request.POST:
            register_form = UserCreationForm(request.POST)
            if not register_form.is_valid():
                return render(request, "views/index.html",
                              {'login_form': AuthenticationForm(None), 'register_form': register_form})


def login_user(request):
    try:
        username = request.POST['email']
        pwd = request.POST['pwd']

        user = authenticate(request, username=username, password=pwd)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login', 'loginError')
    except Exception as e:
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
