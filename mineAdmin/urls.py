
from django.urls import path

from mineAdmin.controllers import *

urlpatterns = [
    path('play', static_controllers.play, name='play'),
    path('stats', static_controllers.stats, name='stats'),
    path('tools', static_controllers.tools, name='tools'),

    path('admin', admin_controllers.index, name='admin'),
    path('admin/users', admin_controllers.users, name='users'),
    path('admin/users/ban', admin_controllers.ban_user, name='ban_user'),
    path('admin/users/update', admin_controllers.update_user, name='change_superuser'),
    path('admin/users/delete', admin_controllers.delete_user, name='delete_user'),

    path('admin/mods', admin_controllers.mods, name='mods'),
    path('admin/mods/new', admin_controllers.new_mod, name='new_mod'),
    path('admin/mods/delete', admin_controllers.delete_mod, name='delete_mod'),
    path('admin/mods/update', admin_controllers.update_mod, name='update_mod'),

    path('admin/server/start', admin_controllers.start_server, name='start_server'),
    path('admin/server/stop', admin_controllers.stop_server, name='stop_server'),

    path('', static_controllers.index, name='index'),
    path('login', login_controllers.login_user, name='login'),
    path('register', login_controllers.register_user, name='register'),
    path('logout', login_controllers.logout_user, name='logout')
]
