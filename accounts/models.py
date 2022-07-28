from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(blank=True, null=True, verbose_name='سن')
    GENDER_CHOICES = (
        ('آقا', 'آقا'),
        ('خانم', 'خانم'),
    )
    gender = models.CharField(max_length=4, choices=GENDER_CHOICES, blank=True, null=True, verbose_name='جنسیت')
    Subscribe_to_the_newsletter = models.BooleanField(default=False, verbose_name='عضویت در خبرنامه')
