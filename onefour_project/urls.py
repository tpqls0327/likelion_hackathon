from django.contrib import admin
from django.urls import path, include
import home.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.views.home, name='home'),
    path('',include('home.urls')),
    path('accounts/', include('account_user.urls')),
    path('manager/', include('account_manager.urls')),
]
