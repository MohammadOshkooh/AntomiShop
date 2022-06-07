from django.urls import path, include

from blog.views import BlogListView, BlogDetailView

app_name = 'blog'

urlpatterns = [
    path('api/', include('blog.api.urls', namespace='blog-api')),
    path('<pk>/', BlogDetailView.as_view(), name='detail'),
    path('', BlogListView.as_view(), name='list'),
]
