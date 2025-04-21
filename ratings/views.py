from rest_framework import generics, permissions
from slant_api.permissions import ReadOnlyIfNotOwner
from ratings.models import Rating
from ratings.serializers import RatingSerializer


class RatingList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RatingDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [ReadOnlyIfNotOwner]
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()
