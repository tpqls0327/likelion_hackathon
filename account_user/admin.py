from django.contrib import admin  
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin  
from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User


# from .models import Profile
from .models import Reservation
from .models import Restaurant

User = get_user_model()

class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ('추가 정보', {'fields': ('ty',),},),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('추가 정보', {
            'fields': ('ty',),
        },),
    )
    

# Register your models here.

# class ProfileInline(admin.StackedInline):  
#     model = Profile
#     can_delete = False
#     verbose_name_plural = 'profile'


# class UserAdmin(BaseUserAdmin):  
#     inlines = (ProfileInline, )


# admin.site.unregister(User)  
admin.site.register(User, UserAdmin)
admin.site.register(Reservation)
admin.site.register(Restaurant)