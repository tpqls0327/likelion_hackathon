from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('signin/', views.signin, name='signin'),
    # path('signin_test/', views.signin_test, name='signin_test'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('kakaologin/<str:test>/', views.kakao_login, name = 'kakaologin'),    
]