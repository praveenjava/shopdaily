# Generated by Django 3.0.8 on 2020-09-01 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0041_auto_20200901_1732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='items',
        ),
        migrations.AddField(
            model_name='item',
            name='items',
            field=models.ManyToManyField(to='store.ShopCart'),
        ),
    ]
