from django.db import models


# Create your models here.

class product(models.Model):
    product_name = models.CharField(max_length=30,null=True)
    product_type = models.CharField(max_length=30,null=True)
    product_price = models.DecimalField(max_digits=10,decimal_places=2,null=True)
    product_discount = models.DecimalField(max_digits=3,decimal_places=0,null=True)
    product_image = models.ImageField(upload_to="p_image",max_length=50,null=True)
    product_main = models.IntegerField(default=0,null=True)

    class Meta:
        db_table = 'product'
