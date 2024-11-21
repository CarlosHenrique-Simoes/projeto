from django.urls import path

from . import views

APP_NAME = 'recipes'

urlpatterns = [
    path('', views.home),
]
