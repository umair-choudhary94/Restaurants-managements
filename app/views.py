from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages
from . models import restaurant,fooditem,MyUser,table,bookingrecord,foodorder,restaurantcategories
from django.db.models import Q
# Create your views here.
def index(request):
    rests = restaurant.objects.all()
    cats = restaurantcategories.objects.all()
    context = {
        "rests" : rests,
        "cats" : cats
    }
    return render(request,"app/index.html",context)
def help(request):
    return redirect(f"https://wa.me/+923437389594?text=I want Some Help")

def register(request):
    # form = NewUserForm()
    return render(request,"register.html")
def login_user(request):
    if request.method == "POST":
        user = request.POST.get("user")
        password = request.POST.get("password")
        userr = authenticate(request,username=user,password=password)
        if userr is not None:
            login(request,userr)
            return redirect("viewprofile")
        else:
            messages.success(request, 'Your username or password is wrong!')
            return redirect("register")
        
    # return render(request,"user/index.html")
def logout_user(request):
    logout(request)
    return redirect("register")
def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        address = request.POST["address"]
        photo = request.FILES.get("photo")
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1 == password2:
            usr = User.objects.create_user(username=username, password=password1,email=email)
            usr.save()
            obj = MyUser.objects.create(user=usr,address=address,photo=photo,phone=phone)
            obj.save()
            user = authenticate(request,username=username,password=password1)

            
            login(request,user)
        else:
            messages.success(request, 'Password not similar')
            return redirect("register")
        
        
       
        return redirect("/register")
@login_required(login_url='/register')   
def viewprofile(request):
    usr = User.objects.get(id=request.user.id)
    objects = bookingrecord.objects.filter(user=usr)
    orders = foodorder.objects.filter(user=usr)
    context = {
        "objects" : objects,
        "orders" : orders
    }
    
    return render(request,"viewprofiel.html",context)
def search(request):
    query = request.GET.get("search")
    if query != "":
        rests = restaurant.objects.filter(
        Q(name__icontains=query) | Q(location__icontains=query) 
    )
                        
    else:
        rests = restaurant.objects.all()
    
    context ={
        "rests" : rests
    }
    return render(request,"result.html",context)
def catsearch(request):
    query = request.GET.get("search")
    cat = restaurantcategories.objects.get(id=query)
    rests = restaurant.objects.filter(category=cat)
    
    context ={
        "rests" : rests
    }
    return render(request,"result.html",context)
def searchfood(request):
    query = request.GET.get("search")
    if query != "":
        items = fooditem.objects.filter(
        Q(title__icontains=query) | Q(price__icontains=query) 
    )
                        
    else:
        items = fooditem.objects.all()
    
    context ={
        "items" : items
    }
    return render(request,"app/foodresult.html",context)

def visitresturants(request,id):
    rest = restaurant.objects.get(id=id)
    tables = table.objects.filter(restaurant=rest)
    total_tables = tables.count()
    seats = 0
    for t in tables:
        seats = seats + t.seats
    items = fooditem.objects.filter(restaurant=rest)
    context = {
        "items" : items,
        "rest" : rest,
        "total_tables" : total_tables,
        "seats" : seats
    }
    return render(request,"app/visitresturants.html",context)
def tables(request,id):
    rest = restaurant.objects.get(id=id)
    tables = table.objects.filter(restaurant=rest)
    context = {
        "rest" : rest,
        "tables" : tables
    }
    return render(request,"app/tables.html",context)
def booknow(request,res,tb):
    tab = table.objects.get(restaurant=res,id=tb)

    tab.booking_status = True
    tab.save()
    rest = restaurant.objects.get(id=res)
    tabl = table.objects.get(id=tb)
    us = User.objects.get(id=request.user.id)
    obj = bookingrecord.objects.create(user=us,restaurant=rest,table=tabl)
    obj.save()
    return redirect("viewprofile")
def orderfood(request,id):
    item = fooditem.objects.get(id=id)
    us = User.objects.get(id=request.user.id)
    obj = foodorder.objects.create(item=item,user=us,bill=item.price)
    obj.save()
    return redirect("viewprofile")
