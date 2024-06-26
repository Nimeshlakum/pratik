# Generated by Django 5.0.4 on 2024-05-03 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_main',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_discount',
            field=models.DecimalField(decimal_places=0, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(max_length=50, null=True, upload_to='p_image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
