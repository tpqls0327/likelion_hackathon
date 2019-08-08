from django.contrib import admin
from django.urls import path, include
from account_user.models import User
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('result/', views.result, name = "result"),
    path('reservation_ok/', views.reservation_ok, name = "reservation_ok"),
    path('reservation/<int:restaurant_id>', views.reservation, name = "reservation"),
    path('info/', views.info, name="info"),
    path('info/<int:restaurant_id>', views.info_real, name="info_real"),
    path('search/', views.search, name="search"),
    path('reservation_list/', views.reservation_list, name = "reservation_list"),
    path('reservation_cancel/', views.reservation_cancel, name = "reservation_cancel"),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
#accounts/login/social/naver/callback/
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

