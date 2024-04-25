from django.urls import path
from myapp.views import *

app_name = 'myapp'

urlpatterns = [

    path ("",main,name="main")


]
