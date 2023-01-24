from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def login_user(request):
    print('...')
    try:
        print('tie que ir')
        username = request.POST['email']
        pwd = request.POST['pwd']

        user = authenticate(request, username=username, password=pwd)
        if user is not None:
            login(request, user)
            print('k')
            return redirect('play')
        else:
            print('va con error')
            return redirect('index', error=True)
    except Exception as e:
        print(e)
        return redirect('play')


def register_user(request):
    username = request.POST['username']
    pwd = request.POST['pwd']

    user = User.objects.create_user(username, 'prueba@prueba', pwd)
    user.save()
    return redirect('index')


def logout_user(request):
    logout(request)
    return redirect('index')
