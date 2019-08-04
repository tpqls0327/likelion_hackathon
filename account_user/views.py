from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

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
            return redirect('/')
        else:
            return render(request, 'accounts/signin.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'accounts/signin.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                request.POST['username'], password=request.POST['password1'])
            user.profile.type = request.POST['type']
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