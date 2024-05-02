from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request,'index.html')

def product_page(request):
    return render(request,'product.html')