from django.contrib import admin
from django.urls import path, include
from . import views

# account_manager
urlpatterns = [
    path('manager_signin/', views.manager_signin, name = 'manager_signin'),
    path('management/', views.management, name = 'management'),
    path('management_reservation_list', views.management_reservation_list, name = 'management_reservation_list'),
    path('management_modify', views.management_modify, name = 'management_modify'),
]