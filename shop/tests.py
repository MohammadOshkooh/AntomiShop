from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from shop.models import Product, ProductCategory
from tag.models import Tag


class ProductTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(username='test user', password='test pass')
        test_tag = Tag.objects.create(title='test tag')
        test_category = ProductCategory.objects.create(title='test category', slug='test-category-slug')
        self.product = Product.objects.create(name='test name', slug='test-slug', availability=True,
                                              old_price=8000000, current_price=7600000, category=test_category,
                                              description='test description',
                                              short_description='test short description')
        self.product.tag.add(test_tag)

    # test def __str__(self):
    def test_string_representation(self):
        product = Product(name='test')
        self.assertEqual(str(product), product.name)

    def test_product_content(self):
        self.assertEqual(self.product.name, 'test name')
        self.assertEqual(self.product.tag.first().title, 'test tag')
        self.assertEqual(self.product.availability, True)
        self.assertEqual(self.product.old_price, 8000000)
        self.assertEqual(self.product.category.title, 'test category')

    def test_product_list_view(self):
        response = self.client.get(reverse('shop:product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/products_list.html')
        self.assertContains(response, 'فروشگاه')

    def test_product_detail_view(self):
        response = self.client.get(reverse('shop:product_detail', kwargs={'slug': 'test-slug'}))
        no_response = self.client.get(reverse('shop:product_detail', kwargs={'slug': 'slug'}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'جزئیات محصول')
        self.assertTemplateUsed(response, 'shop/product_detail.html')

    # def test_product_create_view(self):
    #     response = self.client.post(reverse('shop:product_detail', kwargs={'slug': 't-slug'}), {
    #         'name': 'test name', 'slug': 'test-slug', 'availability': 'True', 'old_price': '8000000',
    #         'current_price': '7600000', 'description': 'test description', 'short_description': 'test short description'
    #     })
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(Product.objects.last().name, 'test name')
