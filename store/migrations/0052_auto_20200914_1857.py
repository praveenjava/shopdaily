# Generated by Django 3.0.8 on 2020-09-14 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0051_auto_20200914_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
