from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def manager_signin(request):
    return render(request, 'manager/manager_signin.html')