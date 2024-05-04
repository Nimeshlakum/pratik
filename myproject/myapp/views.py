from django.shortcuts import render , HttpResponse , redirect
from django.contrib.auth import authenticate , login , logout
from .models import *
from django.contrib.auth.models import *
from django.contrib import messages


def signup(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password')   
        
        try:
            myuser=User.objects.create_user(username,email,pass1)
            myuser.save()
            messages.success(request,"User is Created Please Login")
            return render(request,"login.html")
        
        except:
            pass

    return render(request,"registration.html")

def user_login(request):
    if request.method=="POST":        
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"Login Successful")
            return redirect('/home/')
        else:
            messages.error(request,"Invalid Credentials")
            return render(request,'login.html')  
               
    return render(request,'login.html')

def user_logout(request):
    logout(request)
    return render(request,'login.html')

def registration(request):
    return render(request,'registration.html')

def login_page(request):
    return render(request,'login.html')

def main(request):
    p_deatil = product.objects.all() 
    all = {
        'p_deatil':p_deatil,
    }
    return render(request,'index.html',all)

def product_page(request):
    p_deatil = product.objects.all() 
    all = {
        'p_deatil':p_deatil,
    }
    return render(request,'product.html',all)

def wishlist_page(request):
    p_deatil = product.objects.all() 
    all = {
        'p_deatil':p_deatil,
    }
    return render(request,'wishlist.html',all)

def cart_page(request):
    p_deatil = product.objects.all() 
    all = {
        'p_deatil':p_deatil,
    }
    return render(request,'cart.html',all)

def wishlist(request):
    if request.user.is_authenticated:
        return redirect('/wishlist_page/')
    else:
        return redirect('/login_page/')

def cart(request):
    if request.user.is_authenticated:
        return redirect('/cart_page/')
    else:
        return redirect('/login_page/')