from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def manager_signin(request):
    return render(request, 'manager/manager_signin.html')

def management(request):
    return render(request, 'manager/management.html')

def management_reservation_list(request):
    return render(request, 'manager/management_reservation_list.html')

def management_modify(request):
    return render(request, 'manager/management_modify.html')