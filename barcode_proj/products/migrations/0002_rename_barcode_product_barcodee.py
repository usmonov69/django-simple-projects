# Generated by Django 3.2.7 on 2021-09-30 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='barcode',
            new_name='barcodee',
        ),
    ]