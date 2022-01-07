# Generated by Django 3.2.8 on 2022-01-07 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_products_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='vendor_resell',
        ),
        migrations.AlterField(
            model_name='products',
            name='product_overview',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_price',
            field=models.CharField(max_length=255),
        ),
    ]