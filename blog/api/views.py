from rest_framework.viewsets import ModelViewSet
from .serializers import ArticleSerializers
from ..models import Article
from rest_framework.permissions import IsAdminUser, AllowAny
from .permissions import IsAuthor, IsSuperUser


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializers

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permissions_class = [AllowAny]
        if self.action in ['create']:
            permissions_class = [IsAdminUser]
        else:
            permissions_class = [IsAuthor]
        return [permission() for permission in permissions_class]
