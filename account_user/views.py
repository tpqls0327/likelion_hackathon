from django.shortcuts import render, redirect, HttpResponse
from account_user.models import User
# from django.contrib.auth import login as django_login, logout as django_logout, authenticate
from django.contrib import auth
from .forms import LoginForm
#def signin(request):
#    return render(request, 'accounts/signin.html')

#def signup(request):
#    return render(request, 'accounts/signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            
            print(user)
            return redirect('/')
        else:
            return render(request, 'accounts/signin.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'accounts/signin.html')

def signin_test(request):
    if request.method == 'POST':
        form = LoginForm(request = request, data = request.POST)
        
        user = auth.authenticate(request, username = form['username'], password=form['password'])
        
        if user is not None:
            print(user)
            auth.login(request,user)
            return redirect('/')
        else :
            print(user)
            print('또망함')
            us = request.user
            print(us)
            return HttpResponse(request, 'err')
    else:
        form = LoginForm()
        return render(request, 'accounts/signin(test).html', {'form':form})
            

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                request.POST['username'], password=request.POST['password1'], ty = request.POST['type'])
            auth.login(request, user)
            return redirect('/')
    return render(request, 'accounts/signup.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/')
    return render(request, 'accounts/signup.html')

def kakao_login(request):
    idd = request.POST['id']
    name = request.POST['name']
    email = request.POST['email']
    user = auth.authenticate(request, username=email, password=idd, email = name)
    if user is not None:
        auth.login(request, user)
        return redirect('/')
    else :
        User.objects.create_user(user)
        auth.login(request, user)
        return redirect('/')