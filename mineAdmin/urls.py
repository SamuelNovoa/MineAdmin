from django.urls import path

from mineAdmin import views

urlpatterns = [
    path('', views.index, name='index'),
    path('play', views.play, name='play'),
    path('stats', views.stats, name='stats'),
    path('tools', views.tools, name='tools')
]
