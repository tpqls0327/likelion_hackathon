from django.contrib import admin
from django.urls import path, include
from account_user.models import User
from . import views


urlpatterns = [
    path('result/', views.result, name = "result"),
    path('reservation_ok/', views.reservation_ok, name = "reservation_ok"),
    path('reservation/', views.reservation, name = "reservation"),
    path('info/', views.info, name="info"),
    path('search/', views.search, name="search"),
    path('reservation_list/', views.reservation_list, name = "reservation_list"),
    path('reservation_cancel/', views.reservation_cancel, name = "reservation_cancel"),
]