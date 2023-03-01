from ..forms import CustomAuthenticationForm, CustomCreationForm
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout


def login_user(request):
    try:
        if request.method == 'GET':
            return render(request, 'views/login.html', {'login_form': CustomAuthenticationForm(request, None)})

        elif request.method == 'POST':
            login_form = CustomAuthenticationForm(request, request.POST)
            if not login_form.is_valid():
                return render(request, 'views/login.html', {'login_form': login_form})

            email = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return render(request, 'views/login.html', {'login_form': login_form})

    except Exception as e:
        print(e)
        return render(request, 'views/login.html', {'login_form': CustomAuthenticationForm(None)})


def register_user(request):
    try:
        if request.method == 'GET':
            return render(request, 'views/register.html', {'register_form': CustomCreationForm(None)})

        elif request.method == 'POST':
            register_form = CustomCreationForm(request.POST)
            if not register_form.is_valid():
                return render(request, "views/register.html", {'register_form': register_form})

            user = register_form.save()
            user.save()
            login(request, user)
            return redirect('index')

    except Exception as e:
        print(e)
        return render(request, 'views/register.html', {'register_form': CustomCreationForm(None)})


def logout_user(request):
    logout(request)
    return redirect('index')
