from django.urls import path

from mineAdmin import views

urlpatterns = [
    path('', views.index, name='index'),
    path('play', views.play, name='play'),
    path('stats', views.stats, name='stats'),
    path('tools', views.tools, name='tools'),

    path('login', views.login_user, name='login'),
    path('register', views.register_user, name='register'),
    path('logout', views.logout_user, name='logout')
]
