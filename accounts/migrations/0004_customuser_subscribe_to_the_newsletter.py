# Generated by Django 4.0.4 on 2022-07-28 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_customuser_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='Subscribe_to_the_newsletter',
            field=models.BooleanField(default=False, verbose_name='عضویت در خبرنامه'),
        ),
    ]
