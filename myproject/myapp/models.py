from django.db import models


# Create your models here.

class product(models.Model):
    product_name = models.CharField(max_length=30)
    product_price = models.DecimalField(max_digits=10,decimal_places=2)
    product_discount = models.DecimalField(max_digits=10,decimal_places=2)
    product_image = models.ImageField(upload_to="p_image",max_length=50)

    class Meta:
        db_table = 'product'
