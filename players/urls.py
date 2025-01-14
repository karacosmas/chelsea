from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('list_players/', views.list_players, name = 'list_players'),
]
