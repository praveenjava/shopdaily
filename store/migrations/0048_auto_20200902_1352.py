# Generated by Django 3.0.8 on 2020-09-02 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0047_auto_20200902_1340'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testorder',
            old_name='product',
            new_name='products',
        ),
    ]
