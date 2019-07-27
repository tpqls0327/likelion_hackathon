from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signin(request):
    return render(request, 'accounts/signin.html')

def signup(request):
    return render(request, 'accounts/signup.html')