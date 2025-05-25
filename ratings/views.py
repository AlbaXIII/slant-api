from rest_framework import generics, permissions
from ratings.models import Rating
from ratings.serializers import RatingSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Avg
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


class RatingList(generics.ListCreateAPIView):
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['article']

    def get_queryset(self):
        return Rating.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RatingSerializer
    permission_classes = [permissions.ReadOnlyIfNotOwner]

    def get_queryset(self):
        return Rating.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
class RatingDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RatingSerializer
    permission_classes = [permissions.ReadOnlyIfNotOwner]

    def get_queryset(self):
        return Rating.objects.all()


def article_rating_stats(request, article_id):
    ratings = Rating.objects.filter(article=article_id)

    if ratings.exists():
        avg_rating = ratings.aggregate(Avg('rating'))['rating__avg']
        total_ratings = ratings.count()

        return Response({
            'average_rating': round(avg_rating, 1) if avg_rating else 0,
            'total_ratings': total_ratings,
            'article_id': article_id
        })
    else:
        return Response({
            'average_rating': 0,
            'total_ratings': 0,
            'article_id': article_id
        })
