# Generated by Django 4.0.4 on 2022-06-18 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='product',
            field=models.ManyToManyField(blank=True, to='shop.product', verbose_name='محصول'),
        ),
    ]
