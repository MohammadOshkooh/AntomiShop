from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from shop.models import ProductCategory, Product


class HomePage(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['new_products'] = Product.objects.all().order_by('-id')
        # Most discounts
        # for product in products:
        return context


class AboutUs(TemplateView):
    template_name = 'about_us.html'


class ContactUs(TemplateView):
    template_name = 'contact_us.html'


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)


class FrequentlyAskedQuestions(TemplateView):
    template_name = 'frequently_asked_questions.html'
