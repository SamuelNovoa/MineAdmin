from django.urls import path

from mineAdmin import views

urlpatterns = [
    path('', views.index, name='Index')
]
