# Generated by Django 4.0.4 on 2022-06-08 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_remove_shippingaddress_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='user',
        ),
    ]