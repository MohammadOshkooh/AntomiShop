from django.contrib.auth import get_user_model
from django.db import models

from shop.models import Product


class Cart(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='مالک')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    is_paid = models.BooleanField(default=False, verbose_name='پرداخت شده')

    @property
    def total_price(self):
        total = 0
        for item in self.cart_items.all():
            total += item.total_price
        return total

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد های خرید کاربران'

    def __str__(self):
        return self.owner.username


class Item(models.Model):
    cart = models.ForeignKey(Cart, related_name='cart_items', on_delete=models.CASCADE, verbose_name='سبد خرید')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    price = models.DecimalField(max_digits=18, decimal_places=0, verbose_name='قیمت')
    quantity = models.PositiveIntegerField(default=1, verbose_name='تعداد')

    @property
    def total_price(self):
        return self.price * self.quantity

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'ایتم های سبد های خرید مشتریان'

    def __str__(self):
        return self.product.name
