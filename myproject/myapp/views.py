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
    return render(request,'product.html')