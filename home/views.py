from django.shortcuts import render, HttpResponse
from account_user.models import Restaurant 
from django.db.models import Q

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
    target = request.POST["this_ad"]
    posts = {Restaurant.objects.filter(shop_location_new__contains=target)}
    print(posts)
    return render(request, 'result(real).html', {'posts':posts})

def reservation_list(request):
    return render(request, 'reservation_list.html')

def reservation_cancel(request):
    return render(request, 'reservation_cancel.html')
