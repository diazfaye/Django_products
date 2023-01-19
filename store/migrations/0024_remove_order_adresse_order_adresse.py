# Generated by Django 4.0.4 on 2022-06-15 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0023_alter_order_adresse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='adresse',
        ),
        migrations.AddField(
            model_name='order',
            name='adresse',
            field=models.ManyToManyField(to='store.shippingaddress'),
        ),
    ]
