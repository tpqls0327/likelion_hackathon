from django.shortcuts import render, HttpResponse
from account_user.models import Restaurant, Reservation
from django.db.models import Q
from account_user.models import User as User2
from django.core.paginator import Paginator

def result(request):
    return render(request, 'result.html')

def home(request):
    return render(request, 'home/main.html')

def reservation(request, restaurant_id):
    if request.method == 'POST':
        reservation = Reservation()
        reservation.user = User2.objects.all().get(id=request.user.id)
        reservation.restaurant_id = restaurant_id
        reservation.reser_sum = request.POST['sum']
        reservation.reser_date = request.POST['date']
        reservation.reser_time = request.POST['time']
        reservation.save()
        return render(request, 'reservation_ok.html')
    else:
        return render(request, 'reservation.html')

    
    
def reservation_ok(request):
    return render(request, 'reservation_ok.html')

def info(request):
    return render(request, 'info.html')
def info_real(request, restaurant_id):
    info = Restaurant.objects.get(pk=restaurant_id)
    return render(request, 'info(real).html', {'info':info})


def search(request):
    target = request.POST["this_ad"]
    things = Restaurant.objects.filter(shop_location_new__contains=target)
    paginator = Paginator(things, 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'result(real).html', {'posts':posts})

def reservation_list(request):
    return render(request, 'reservation_list.html')



def reservation_cancel(request):
    return render(request, 'reservation_cancel.html')

def about(request):
    return render(request, 'about.html')
