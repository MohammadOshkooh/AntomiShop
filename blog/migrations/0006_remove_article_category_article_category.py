# Generated by Django 4.0.4 on 2022-05-30 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_articlecategory_article_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='category',
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(blank=True, null=True, to='blog.articlecategory', verbose_name='دسته بندی'),
        ),
    ]
