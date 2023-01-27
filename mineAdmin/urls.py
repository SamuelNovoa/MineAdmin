
from django.urls import path

from mineAdmin.controllers import *

urlpatterns = [
    path('play', static_controllers.play, name='play'),
    path('stats', static_controllers.stats, name='stats'),
    path('tools', static_controllers.tools, name='tools'),

    path('', login_controllers.index, name='index'),
    # path('login', login_controller.login_user, name='login'),
    # path('login/<str:error>', public_controller.index, name='login'),
    path('register', login_controllers.register_user, name='register'),
    path('logout', login_controllers.logout_user, name='logout')
]
