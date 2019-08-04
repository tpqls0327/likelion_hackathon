from django.shortcuts import render
from account_user.models import Restaurant 

def result(request):
    return render(request, 'result.html')

def home(request):
    return render(request, 'home/main.html')

def reservation(request):
    return render(request, 'reservation.html')
    
def reservation_ok(request):
    return render(request, 'reservation_ok.html')

def info(request):
    return render(request, 'info.html')

def search(request):
    posts = list()
    target = request.GET['address']
    things = Restaurant.objects.all()
    for thing in things:
        if (target in thing.shop_location_new) or (target in thing.shop_location_old):
            posts.append(thing)
    return render(request, 'result(real).html', {'posts',posts,})