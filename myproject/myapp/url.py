from django.urls import path
from myapp.views import *

app_name = 'myapp'

urlpatterns = [

    path ("",main,name="main"),
    path ("home/",main,name="main"),
    path ("product_page/",product_page,name="product_page"),
    path ("wishlist_page/",product_page,name="wishlist_page"),
    path ("cart_page/",product_page,name="cart_page")


]
