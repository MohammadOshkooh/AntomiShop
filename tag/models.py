from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=200, verbose_name='برچسب')

    class Meta:
        verbose_name = 'برچسب'
        verbose_name_plural = 'برچسب ها'

    def __str__(self):
        return self.title
