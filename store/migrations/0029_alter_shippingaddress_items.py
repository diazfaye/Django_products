# Generated by Django 4.0.4 on 2022-06-15 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0028_remove_shippingaddress_cart_shippingaddress_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='items',
            field=models.CharField(max_length=300),
        ),
    ]