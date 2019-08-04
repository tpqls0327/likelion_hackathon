from django.contrib import admin
from django.urls import path, include
from . import views

# account_manager
urlpatterns = [
    path('manager_signin/', views.manager_signin, name = 'manager_signin'),
]