# Generated by Django 4.0.4 on 2022-05-22 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_productcategory_fullname_alter_favorite_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcategory',
            name='fullname',
        ),
    ]
