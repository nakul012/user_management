from asyncio.windows_events import NULL
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib import admin
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    pass


class UserProfile(models.Model):
    user = models.OneToOneField('user_management.User', on_delete= models.PROTECT)
    phone_number = PhoneNumberField(blank=True,null=True)
    profile_pic=models.ImageField(upload_to="photos/%Y/%m/%d",blank=True,null=True) 
    gender = models.CharField(max_length=140,blank=True,null=True)


    @property
    def address(self):
        return self.address_set.all()


    @property
    def hobbies(self):
        return self.hobbies_set.all()


class Hobbies(models.Model):
    profile = models.ManyToManyField('user_management.UserProfile')
    name = models.CharField(max_length=140)

class Address(models.Model):
    profile = models.ForeignKey('user_management.UserProfile', on_delete= models.CASCADE)
    address = models.CharField(max_length=500, blank=False,null=False)
    is_default=models.BooleanField(default=False)



admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Hobbies)
admin.site.register(Address)


