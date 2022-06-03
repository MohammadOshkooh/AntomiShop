from django.urls import path

from blog.views import BlogListView, BlogDetailView

app_name = 'blog'

urlpatterns = [
    path('<pk>/', BlogDetailView.as_view(), name='detail'),
    path('', BlogListView.as_view(), name='list'),
]
