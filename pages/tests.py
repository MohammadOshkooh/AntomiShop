from django.test import TestCase
from django.urls import reverse, resolve

from pages.views import HomePage, AboutUs, ContactUs


class HomePageTest(TestCase):
    def setUp(self) -> None:
        self.url = reverse('home')
        self.response = self.client.get(self.url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_homepage_contain_correct_html(self):
        self.assertContains(self.response, 'ارسال رایگان')

    # view test
    def test_homepage_view(self):
        view = resolve(self.url)
        self.assertEqual(view.func.__name__, HomePage.as_view().__name__)


class AboutUsPageTest(TestCase):
    def setUp(self) -> None:
        self.url = reverse('about_us')
        self.response = self.client.get(self.url)

    def test_aboutus_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutus_page_template(self):
        self.assertTemplateUsed(self.response, 'about_us.html')

    def test_aboutus_page_contain_correct_html(self):
        self.assertContains(self.response, 'درباره ما')

    def test_aboutus_view(self):
        view = resolve(self.url)
        self.assertEqual(view.func.__name__, AboutUs.as_view().__name__)


class ContactUsTest(TestCase):
    def setUp(self) -> None:
        self.url = reverse('contact_us')
        self.response = self.client.get(self.url)

    def test_contactus_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_contactus_page_template(self):
        self.assertTemplateUsed(self.response, 'contact_us.html')

    def test_contactus_page_contain_correct_html(self):
        self.assertContains(self.response, 'تماس با ما')

    def test_contactus_view(self):
        view = resolve(self.url)
        self.assertEqual(view.func.__name__, ContactUs.as_view().__name__)
