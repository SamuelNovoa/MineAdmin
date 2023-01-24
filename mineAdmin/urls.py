from django.urls import path

from mineAdmin.controllers import *

urlpatterns = [
    path('', public_controller.index, name='index'),
    path('<error>', public_controller.index, name='index'),
    path('play', public_controller.play, name='play'),
    path('stats', public_controller.stats, name='stats'),
    path('tools', public_controller.tools, name='tools'),

    path('login', login_controller.login_user, name='login'),
    path('register', login_controller.register_user, name='register'),
    path('logout', login_controller.logout_user, name='logout')
]
