# Generated by Django 3.0.8 on 2020-09-01 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0040_auto_20200901_1716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='items',
        ),
        migrations.AddField(
            model_name='item',
            name='items',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.ShopCart'),
            preserve_default=False,
        ),
    ]