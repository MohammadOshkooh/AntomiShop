from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import UpdateView
from .models import CustomUser


class Dashboard(UpdateView, SuccessMessageMixin, LoginRequiredMixin):
    template_name = 'dashboard.html'
    model = get_user_model()
    fields = ['username', 'email', 'first_name', 'last_name', 'age', 'gender', 'Subscribe_to_the_newsletter']
    success_message = 'تغییرات با موفقیت اعمال شد.'

    def get_success_url(self):
        pk = self.request.user.pk
        return f'/accounts/dashboard/{pk}/'