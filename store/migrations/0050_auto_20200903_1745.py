# Generated by Django 3.0.8 on 2020-09-03 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0049_auto_20200902_1355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='order',
            name='first_name',
            field=models.CharField(max_length=11),
        ),
    ]
