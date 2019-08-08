from django.db import models  
from django.contrib.auth.models import AbstractUser, UserManager as BaseUserManager
from django.db.models.signals import post_save  
from django.dispatch import receiver


# class Profile(models.Model):  
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     givenname = models.CharField(max_length=50, null= True)
#     type = models.CharField(max_length=1, null = True)
#     logined_at = models.DateTimeField(blank=True, null=True)
#     updated_at = models.DateTimeField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     user_comments = models.DateTimeField(blank=True, null=True)

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):  
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):  
#     instance.profile.save()

class UserManager(BaseUserManager):
    def create_superuser(self, *args, **kwargs):
        return super().create_superuser(ty = '0', *args, **kwargs)
    
    # def create_user(self, *args, **kwargs):
    #     return super().create_user(type = '0', *args, **kwargs)

class User(AbstractUser):

    ty = models.IntegerField(null = True)

    objects = UserManager()

    def __str__(self):
        return self.username


class Reservation(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null = True)
    restaurant_id = models.IntegerField(blank=True, null=True)
    reser_sum = models.IntegerField(blank=True, null=True)
    reser_date = models.CharField(max_length=20, null=True)
    reser_time = models.CharField(max_length=20, null=True)

class Restaurant(models.Model):
    shopname = models.CharField(max_length=20)
    profile_img = models.ImageField(blank=True, null=True)
    food_img1 = models.ImageField(blank=True, null=True)
    food_img2 = models.ImageField(blank=True, null=True)
    food_img3 = models.ImageField(blank=True, null=True)
    shop_description = models.TextField(blank=True, null=True)
    food_description = models.TextField(blank=True, null=True)
    shop_location_new = models.CharField(max_length=250, blank=True, null=True)
    shop_location_old = models.CharField(max_length=250, blank=True, null=True)
    shop_comments = models.TextField(blank=True, null=True)
    shop_owner = models.ForeignKey(User,on_delete=models.CASCADE, null = True)
class nothing():
    nothing = 0
        
