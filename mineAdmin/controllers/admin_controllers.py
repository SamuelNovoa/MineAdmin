from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect

from mineAdmin.forms import ModForm
from mineAdmin.models import Mod, User
from mineAdmin.services import ServerService


def superuser_check(user):
    return user.is_superuser


@user_passes_test(superuser_check)
def index(request):
    try:
        if request.method == 'GET':
            server = ServerService()
            return render(request, 'views/admin_global.html', {
                'available': server.available,
                'running': server.running,
                'last_log': server.last_log
            })
        elif request.method == 'POST':
            pass
    except Exception as e:
        print(e)

@user_passes_test(superuser_check)
def users(request):
    try:
        if request.method == 'GET':
            server = ServerService()
            return render(request, 'views/admin_users.html', {
                'available': server.available,
                'superusers': User.objects.filter(is_superuser=True, is_active=True),
                'users': User.objects.filter(is_superuser=False, is_active=True),
                'blocked': User.objects.filter(is_active=False)
            })
        elif request.method == 'POST':
            pass
    except Exception as e:
        print(e)

@user_passes_test(superuser_check)
def ban_user(request):
    try:
        if request.method != 'POST':
            return redirect('users')

        user_id = request.POST.get('user_id', 0)
        if user_id == 0:
            return redirect('users')

        user = User.objects.get(id=user_id)
        user.is_active = not user.is_active
        user.save()
        return redirect('users')
    except Exception as e:
        print(e)

@user_passes_test(superuser_check)
def delete_user(request):
    try:
        if request.method != 'POST':
            return redirect('users')

        user_id = request.POST.get('user_id', 0)
        if user_id == 0:
            return redirect('users')

        User.objects.get(id=user_id).delete()
        return redirect('users')
    except Exception as e:
        print(e)


@user_passes_test(superuser_check)
def update_user(request):
    try:
        if request.method != 'POST':
            return redirect('users')

        user_id = request.POST.get('user_id', 0)
        if user_id == 0:
            return redirect('users')

        user = User.objects.get(id=user_id)
        user.is_superuser = not user.is_superuser
        user.save()
        return redirect('users')
    except Exception as e:
        print(e)


@user_passes_test(superuser_check)
def mods(request):
    try:
        if request.method == 'GET':
            server = ServerService()
            return render(request, 'views/admin_mods.html', {
                'available': server.available,
                'enabled_mods': server.enabled_mods,
                'disabled_mods': server.disabled_mods,
                'mod_form': ModForm()
            })
    except Exception as e:
        print(e)


@user_passes_test(superuser_check)
def new_mod(request):
    try:
        if request.method != 'POST':
            return

        mod_form = ModForm(request.POST)
        if not mod_form.is_valid():
            server = ServerService()
            return render(request, "views/admin_mods.html", {
                'available': server.available,
                'enabled_mods': server.enabled_mods,
                'disabled_mods': server.disabled_mods,
                'mod_form': mod_form
            })

        mod = mod_form.save()
        mod.save()
        return redirect('mods')
    except Exception as e:
        print(e)


@user_passes_test(superuser_check)
def delete_mod(request):
    try:
        if request.method != 'POST':
            return redirect('mods')

        mod_id = request.POST.get('mod_id', 0)
        if mod_id == 0:
            return redirect('mods')

        Mod.objects.filter(id=mod_id).delete()
        return redirect('mods')
    except Exception as e:
        print(e)


@user_passes_test(superuser_check)
def update_mod(request):
    try:
        if request.method != 'POST':
            return redirect('mods')

        mod_id = request.POST.get('mod_id', 0)
        if mod_id == 0:
            return redirect('mods')

        mod = Mod.objects.get(id=mod_id)
        mod.active = True if request.POST.get('active', 'false') == 'false' else False
        mod.save()
        return redirect('mods')
    except Exception as e:
        print(e)


@user_passes_test(superuser_check)
def start_server(request):
    return redirect('admin')


@user_passes_test(superuser_check)
def stop_server(request):
    return redirect('admin')
