from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
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

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'owner',
        'owner__article__owner__profile',
        'favourites__owner__profile',
        'owner__comment__owner__profile',
        'owner__profile',
    ]

    search_fields = [
        'owner__username',
        'title',
        'subject',
    ]

    ordering_fields = [
        'favourites_count',
        'comments_count',
        'favourites__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [ReadOnlyIfNotOwner]
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
