from rest_framework import generics, permissions
from slant_api.permissions import ReadOnlyIfNotOwner
from favourites.models import Favourite
from favourites.serializers import FavouriteSerializer


class FavouriteList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FavouriteSerializer
    queryset = Favourite.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FavouriteDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [ReadOnlyIfNotOwner]
    serializer_class = FavouriteSerializer
    queryset = Favourite.objects.all()
