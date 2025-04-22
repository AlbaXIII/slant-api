from django.db.models import Count
from rest_framework import generics, permissions
from .models import Article
from .serializers import ArticleSerializer
from slant_api.permissions import ReadOnlyIfNotOwner


class ArticleList(generics.ListCreateAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Article.objects.annotate(
        favourites_count=Count('favourites', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_on')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [ReadOnlyIfNotOwner]
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
