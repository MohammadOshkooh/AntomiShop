from django.urls import path

from pages.views import HomePage, AboutUs, ContactUs, FrequentlyAskedQuestions

urlpatterns = [
    path('about-us/', AboutUs.as_view(), name='about_us'),
    path('contact_us/', ContactUs.as_view(), name='contact_us'),
    path('questions/', FrequentlyAskedQuestions.as_view(), name='questions'),
    path('', HomePage.as_view(), name='home'),
]
