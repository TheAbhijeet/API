from rest_framework import generics
from .models import user_profile
from .serializers import user_profile_serializer


class user_create(generics.ListCreateAPIView):
    serializer_class = user_profile_serializer
    queryset = user_profile.objects.all()
