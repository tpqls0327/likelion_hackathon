from django.contrib import admin
from django.urls import path, include
from . import views
from account_user import models

# account_manager
urlpatterns = [
    path('manager_signin/', views.manager_signin, name = 'manager_signin'),
    path('management/', views.management, name = 'management'),
    path('management_reservation_list/<int:restaurant_id>', views.management_reservation_list, name = 'management_reservation_list'),
    path('management_modify', views.management_modify, name = 'management_modify'),
    path('Restaurant_register', views.Restaurant_register, name = 'Restaurant_register'),
]