from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(product)

# class product(admin.ModelAdmin):
#   list_display = ("product_name", "product_price", "product_discount","product_image")
