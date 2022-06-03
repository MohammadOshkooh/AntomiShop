from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse, resolve

from accounts.views import Dashboard


class DashboardTest(TestCase):
    def setUp(self) -> None:
        user = get_user_model().objects.create(username='test user', password='test pass')
        self.url = reverse('accounts:dashboard', kwargs={'pk': user.pk})
        self.response = self.client.get(self.url)

    def test_dashboard_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_dashboard_page_template(self):
        self.assertTemplateUsed(self.response, 'dashboard.html')

    def test_dashboard_page_correct_html(self):
        self.assertContains(self.response, 'حساب کاربری')

    def test_dashboard_page_view(self):
        view = resolve(self.url)
        self.assertEqual(view.func.__name__, Dashboard.as_view().__name__)
