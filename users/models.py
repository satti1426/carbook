from django.db import models
from django.contrib.auth.models import AbstractUser


from .constants import *
# Create your models here.
carstype=[
    ("petrol","petrol"),
    ("deisel","deisel"),
    ("cng","cng")
]

class CommonField(models.Model):
    created_on = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_on = models.DateTimeField(auto_now=True,null=True,blank=True)

class User(AbstractUser):
    email = models.EmailField(unique=True,blank=True,null=True)
    role_id = models.PositiveIntegerField(default=USER,choices=USER_ROLE,null=True,blank=True)

    created_on = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_on = models.DateTimeField(auto_now=True,null=True,blank=True)

  

class Comapany(CommonField):
     user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
     name = models.CharField(max_length=255,null=True,blank=True)
     created_ons = models.DateTimeField(auto_now_add=True,blank=True,null=True)

     def __str__(self):
         return self.name


class Car(CommonField):
    company=models.ForeignKey(Comapany,on_delete=models.CASCADE,null=True,blank=True)  
    model = models.CharField(max_length=50,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    car_name=models.CharField(max_length=255,blank=True,null=True)
    car_type = models.PositiveIntegerField(choices=CAR_TYPE,null=True,blank=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name='user_cars')


class notification(models.Model):
    created_for=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name='users')
    created_by=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=200,null=True,blank=True)
    decs=models.TextField(null=True,blank=True)