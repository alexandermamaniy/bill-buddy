from rest_framework import generics
from buddy_profiles.models import BuddyProfile
from buddy_profiles.serializers import BuddyProfileSerializer

class BuddyProfileListCreateView(generics.ListCreateAPIView):
    queryset = BuddyProfile.objects.all()
    serializer_class = BuddyProfileSerializer

class BuddyProfileRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BuddyProfile.objects.all()
    serializer_class = BuddyProfileSerializer
