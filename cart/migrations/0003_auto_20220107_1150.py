# Generated by Django 3.2.8 on 2022-01-07 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20220107_1117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='device_id',
        ),
        migrations.AddField(
            model_name='cart',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=50),
        ),
    ]
