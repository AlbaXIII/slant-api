from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer
from slant_api.permissions import ReadOnlyIfNotOwner


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [ReadOnlyIfNotOwner]
    queryset = Profile.objects.all()
