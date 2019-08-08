from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from account_user.models import User as User2
from django.contrib import auth
from account_user.models import Restaurant, Reservation
from django.core.paginator import Paginator

# Create your views here.

def manager_signin(request):
    return render(request, 'manager/manager_signin.html')

def management(request):
    somethings = Restaurant.objects.all().filter(shop_owner = User2.objects.all().get(id=request.user.id))
    paginator = Paginator(somethings,5)
    page = request.GET.get('page')
    things = paginator.get_page(page)
        
    return render(request, 'manager/management.html', {'things':things,})

def management_reservation_list(request, restaurant_id):
    somethings = Reservation.objects.all().filter(restaurant_id = restaurant_id)
    paginator = Paginator(somethings,5)
    page = request.GET.get('page')
    things = paginator.get_page(page)

    return render(request, 'manager/management_reservation_list.html', {'things':things,})

def management_modify(request):
    if request.method =='POST':
        restaurant = Restaurant()
        restaurant.shopname = request.POST['shopname']
        restaurant.profile_img = request.POST['profile_img']
        restaurant.food_img1 = request.POST['food_img1']
        restaurant.food_img2 = request.POST['food_img2']
        restaurant.food_img3 = request.POST['food_img3']
        restaurant.shop_description = request.POST['shop_description']
        restaurant.food_description = request.POST['food_description']
        restaurant.shop_location_new = request.POST['shop_location_new']
        restaurant.shop_location_old = request.POST['shop_location_new']
        restaurant.shop_owner = User2.objects.all().get(id=request.user.id)
        restaurant.save()

    return render(request, 'manager/management_modify.html')

def Restaurant_register(request):
    if request.method =='POST':
        restaurant = Restaurant()
        restaurant.shopname = request.POST['shopname']
        restaurant.profile_img = request.POST['profile_img']
        restaurant.food_img1 = request.POST['food_img1']
        restaurant.food_img2 = request.POST['food_img2']
        restaurant.food_img3 = request.POST['food_img3']
        restaurant.shop_description = request.POST['shop_description']
        restaurant.food_description = request.POST['food_description']
        restaurant.shop_location_new = request.POST['shop_location_new']
        restaurant.shop_location_old = request.POST['shop_location_new']
        restaurant.shop_owner = User2.objects.all().get(id=request.user.id)
        restaurant.save()
        return redirect('/manager/management')
    else :
        return render(request, 'manager/Restaurant_register.html')

    return render(request, 'manager/Restaurant_register.html')