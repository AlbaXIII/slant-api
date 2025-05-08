from rest_framework import generics, filters
from django.db.models import Count
from .models import Profile
from .serializers import ProfileSerializer
from slant_api.permissions import ReadOnlyIfNotOwner


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.annotate(
        articles_count=Count('owner__article', distinct=True),
        rating_count=Count('owner__rating', distinct=True)
    ).order_by('-created_on')

    serializer_class = ProfileSerializer

    filter_backends = [
        filters.OrderingFilter,
    ]

    ordering_fields = [
        'articles_count',
        'rating_count',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [ReadOnlyIfNotOwner]
    queryset = Profile.objects.annotate(
        articles_count=Count('owner__article', distinct=True),
        rating_count=Count('owner__rating', distinct=True)
    ).order_by('-created_on')
    serializer_class = ProfileSerializer
