# Generated by Django 5.0.4 on 2024-05-02 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_discount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_image', models.ImageField(max_length=50, upload_to='p_image')),
            ],
            options={
                'db_table': 'product',
            },
        ),
    ]
