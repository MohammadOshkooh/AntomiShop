# Generated by Django 4.0.4 on 2022-05-30 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_article_image_alter_article_file_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gallery',
            old_name='product',
            new_name='article',
        ),
    ]
