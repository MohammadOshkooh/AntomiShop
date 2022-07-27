from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from tag.models import Tag


class ProductCategory(models.Model):
    parent = models.ForeignKey('self', related_name='child', on_delete=models.CASCADE, blank=True, null=True,
                               verbose_name='پدر')
    title = models.CharField(max_length=400, verbose_name='دسته بندی محصول')
    active = models.BooleanField(default=True)
    slug = models.SlugField()

    def get_fullname(self):
        fullname = self.title
        current = self
        while current.parent is not None:
            fullname += '-'
            fullname += current.parent.title
            current = current.parent
        return fullname

    def __str__(self):
        return f"{self.parent}-{self.title}"

    class Meta:
        verbose_name = 'دسته بندی محصولات'
        verbose_name_plural = 'دسته بندی های محصولات'

    def all_parent(self):
        categories = []
        current_category = self
        while current_category is not None:
            categories.append(current_category)
            current_category = current_category.parent
        return categories


    def all_children(self):
        children = []
        children_count = 0
        all_categories = ProductCategory.objects.all()
        for category in all_categories:
            all_parent = category.all_parent()
            if all_parent[-1] == self and len(all_parent) > children_count:
                children = all_parent
                children_count = len(all_parent)
        return children

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.slug])


class Product(models.Model):
    name = models.CharField(max_length=300, verbose_name='نام محصول')
    old_price = models.IntegerField(verbose_name='قیمت قبلی')
    current_price = models.IntegerField(verbose_name='قیمت جدید')
    short_description = models.TextField(verbose_name='توضیحات کوتاه')
    description = models.TextField(verbose_name='توضیحات')
    availability = models.BooleanField(default=True, verbose_name='موجود/ناموجود')
    slug = models.SlugField()
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, blank=True,
                                 verbose_name='دسته بندی محصول')
    tag = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.slug])

    def average_product_rating(self):
        comments = self.comment_set.filter(is_active=True)
        if comments.count() == 0:
            return 0
        s = 0
        for comment in comments:
            s += comment.product_rating

        return int(s / comments.count())

    def get_average_blank_star(self):
        avg = self.average_product_rating()
        return 5 - avg

    def get_discount(self):
        return int(((self.old_price - self.current_price) / self.old_price) * 100)


class Gallery(models.Model):
    image = models.ImageField(upload_to='products/%y/%m/%d/', null=True, blank=True, verbose_name='تصویر محصول')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'گالری تصاویر'
        verbose_name_plural = 'گالری تصاویر'


STATUS_CHOICES = (
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)


class Favorite(models.Model):
    owner = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, verbose_name='مالک')
    product = models.ManyToManyField(Product, blank=True, verbose_name='محصول')

    def __str__(self):
        return self.owner.username

    class Meta:
        verbose_name = 'علاقه مندی'
        verbose_name_plural = 'علاقه مندی ها'


class Comment(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='نام شخص')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    comment = models.TextField(verbose_name='نقد و بررسی شما')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    product_rating = models.IntegerField(choices=STATUS_CHOICES, default="", verbose_name='امتیاز شما')
    is_active = models.BooleanField(default=True, verbose_name='فعال')

    def get_blank_star(self):
        return 5 - self.product_rating

    def __str__(self):
        return self.owner.username

    class Meta:
        verbose_name = 'نقد و بررسی محصولات'
        verbose_name_plural = 'نقد و بررسی های محصولات'
