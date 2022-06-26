from audioop import reverse

from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, FormView

from config import settings
from pages.forms import ContactUsForm
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


class ContactUs(FormView):
    template_name = 'contact_us.html'
    form_class = ContactUsForm

    def form_valid(self, form):
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')
        title = form.cleaned_data.get('title')
        body = f'{name}\n{message}'
        email_form = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail(title, body, email_form, recipient_list)
        messages.success(self.request, 'نظر شما با موفقیت ارسال شد')
        return redirect(reverse_lazy('contact_us'))


def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)


class FrequentlyAskedQuestions(TemplateView):
    template_name = 'frequently_asked_questions.html'
