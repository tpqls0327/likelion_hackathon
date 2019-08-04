from django.db import models  
from django.contrib.auth.models import User  
from django.db.models.signals import post_save  
from django.dispatch import receiver

class Profile(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    givenname = models.CharField(max_length=50, null= True)
    type = models.CharField(max_length=1, null = True)
    logined_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    user_comments = models.DateTimeField(blank=True, null=True)
    class Meta:
        db_table = 'member'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):  
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):  
    instance.profile.save()


class Reservation(models.Model):
    member_id = models.IntegerField(blank=True, null=True)
    restaurant_id = models.IntegerField(blank=True, null=True)
    reser_sum = models.IntegerField(blank=True, null=True)
    resr_status = models.CharField(max_length=1)
    reser_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reservation'

class Restaurant(models.Model):
    shopname = models.CharField(max_length=20)
    profile_img = models.CharField(max_length=250, blank=True, null=True)
    food_img1 = models.CharField(max_length=250, blank=True, null=True)
    food_img2 = models.CharField(max_length=250, blank=True, null=True)
    food_img3 = models.CharField(max_length=250, blank=True, null=True)
    shop_description = models.TextField(blank=True, null=True)
    food_description = models.TextField(blank=True, null=True)
    shop_location = models.CharField(max_length=250, blank=True, null=True)
    shop_comments = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'restaurant'