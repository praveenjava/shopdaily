# Generated by Django 3.0.8 on 2020-08-28 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0023_auto_20200828_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]