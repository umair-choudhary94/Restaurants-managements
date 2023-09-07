from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class MyUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    
    address = models.CharField(max_length=1000,default="nothing")
    photo = models.ImageField(null=False,blank=False,upload_to="user")
    phone = models.CharField(max_length=1000,default="nothing")
    trusted = models.BooleanField(default=False)
class restaurantcategories(models.Model):
    category = models.CharField(max_length=400,default="Nothing")
    def __str__(self) -> str:
        return self.category
class restaurant(models.Model):
    name = models.CharField(max_length=1000,default="Nothing")
    location = models.CharField(max_length=100,default="Nothing")
    category = models.ForeignKey(restaurantcategories, on_delete=models.CASCADE,default=1)
    min_price = models.IntegerField(default=0)
    max_price = models.IntegerField(default=0)
    seats = models.IntegerField(default=0)
    tables = models.IntegerField(default=0)
    photo = models.ImageField(null=False,blank=False)
    def __str__(self) -> str:
        return self.name

class fooditem(models.Model):
    restaurant = models.ForeignKey(restaurant, on_delete=models.CASCADE,default=1)
    title = models.CharField(max_length=1000,default="Nothing")
    price = models.IntegerField(default=0)
    photo = models.ImageField(null=False,blank=False,upload_to="food")
    def __str__(self) -> str:
        return self.title

class table(models.Model):
    restaurant = models.ForeignKey(restaurant, on_delete=models.CASCADE,default=1)
    seats = models.IntegerField(default=0)
    booking_status = models.BooleanField(default=False)
    

class bookingrecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    restaurant = models.ForeignKey(restaurant, on_delete=models.CASCADE,default=1)
    table = models.ForeignKey(table, on_delete=models.CASCADE,default=1)
    timestamp = models.DateTimeField(auto_now_add=True)

class foodorder(models.Model):
    item = models.ForeignKey(fooditem, on_delete=models.CASCADE,default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    bill = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    order_status = models.BooleanField(default=False)

