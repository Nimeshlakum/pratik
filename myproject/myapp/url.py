from django.urls import path
from myapp.views import *

app_name = 'myapp'

urlpatterns = [

    path ("",main,name="main"),
    path ("product_page/",product_page,name="product_page")


]
