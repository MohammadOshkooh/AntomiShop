from django.urls import path, include
from rest_framework import routers
from .views import ArticleViewSet

app_name = 'blog_api'

router = routers.SimpleRouter()

router.register('', ArticleViewSet, basename='article')

urlpatterns = [
    path('', include(router.urls)),
]
