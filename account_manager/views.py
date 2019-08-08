from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from account_user.models import Restaurant

# Create your views here.

def manager_signin(request):
    return render(request, 'manager/manager_signin.html')

def management(request):
    return render(request, 'manager/management.html')

def management_reservation_list(request):
    return render(request, 'manager/management_reservation_list.html')

def management_modify(request):
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
        restaurant.shop_owner = request.user
        restaurant.save()
        return render(request,'home/main.html')
    else :
        return render(request, 'manager/Restaurant_register.html')

    return render(request, 'manager/Restaurant_register.html')