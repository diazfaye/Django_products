# Generated by Django 4.0.4 on 2022-06-08 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_visiteur_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='visiteur',
            name='city',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='visiteur',
            name='state',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='visiteur',
            name='zipcode',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]