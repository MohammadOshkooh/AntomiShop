from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from blog.models import Article


class BlogTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(username='test user', password='test pass')
        self.article = Article.objects.create(title='test title', author=self.user, body='this is a test')

    def test_string_representation(self):
        self.assertEqual(str(self.article), self.article.title)

    def test_article_content(self):
        self.assertEqual(self.article.title, 'test title')
        self.assertEqual(self.article.author, self.user)
        self.assertEqual(self.article.body, 'this is a test')

    def test_article_list_view(self):
        response = self.client.get(reverse('blog:list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog.html')

    def test_article_detail_view(self):
        response = self.client.get(reverse('blog:detail', kwargs={'pk': self.article.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog_details.html')
        no_response = self.client.get(reverse('blog:detail', kwargs={'pk': '44655'}))
        self.assertEqual(no_response.status_code, 404)
