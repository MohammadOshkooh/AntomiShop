from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from tag.models import Tag


class ArticleCategory(models.Model):
    title = models.CharField(max_length=250, verbose_name='عنوان')
    slug = models.SlugField(verbose_name='اسلاگ')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=500, verbose_name='عنوان')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='نویسنده')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')
    body = models.TextField(verbose_name='متن مقاله')
    tag = models.ManyToManyField(Tag, blank=True, null=True, verbose_name='برچسب')
    file = models.FileField(upload_to='blog/file/%Y/%m/%d/', null=True, blank=True, verbose_name='فایل')
    category = models.ManyToManyField(ArticleCategory, verbose_name='دسته بندی', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('blog:detail', args=[self.pk])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقاله ها'


class BlogComment(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='نام شخص')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='مقاله')
    comment = models.TextField(verbose_name='کامنت')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    is_active = models.BooleanField(default=True, verbose_name='فعال')
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    def is_child(self, parent):
        """
        return: self is_child parent
        """
        while self.parent is not None:
            if self.parent == parent:
                return True
            else:
                self = self.parent
        return False

    def get_all_children(self):
        children = []
        for comment in BlogComment.objects.all():
            if comment.is_child(self):
                children.append(comment)
        return children

    def __str__(self):
        return self.owner.username

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'


class Gallery(models.Model):
    image = models.ImageField(upload_to='blog/image/%Y/%m/%d/', null=True, blank=True, verbose_name='تصویر')
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.article.title

    class Meta:
        verbose_name = 'گالری تصاویر'
        verbose_name_plural = 'گالری تصاویر'
