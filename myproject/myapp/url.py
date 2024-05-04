from django.urls import path
from myapp.views import *

app_name = 'myapp'

urlpatterns = [

    path ("",main,name="main"),
    path ("home/",main,name="main"),

    path("login_page/",login_page),
    path("login/",user_login),

    path("logout/",user_logout),

    path("registration_page/",registration),
    path("registration/",signup),

    path ("product_page/",product_page,name="product_page"),
    path ("wishlist_page/",wishlist_page,name="wishlist_page"),
    path ("cart_page/",cart_page,name="cart_page"),

    path ("wishlist/",wishlist,name="wishlist"),
    path ("cart/",cart,name="cart")

]
