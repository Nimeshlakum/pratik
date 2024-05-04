from django.shortcuts import render 
from .models import *

# Create your views here.

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
    return render(request,'product.html',all)

def cart_page(request):
    p_deatil = product.objects.all() 
    all = {
        'p_deatil':p_deatil,
    }
    return render(request,'product.html',all)