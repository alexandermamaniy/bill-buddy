from rest_framework import generics, status
from rest_framework.generics import RetrieveAPIView, CreateAPIView

from buddy_profiles.models import BuddyProfile
from buddy_profiles.serializers import BuddyProfileSerializer
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class BuddyProfileListCreateView(generics.ListCreateAPIView):
    queryset = BuddyProfile.objects.all()
    serializer_class = BuddyProfileSerializer


class BuddyProfileRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BuddyProfile.objects.filter(is_active=True)
    serializer_class = BuddyProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.deleted_date = timezone.now()
        instance.save()
        user = instance.user
        user.is_active = False
        user.deleted_date = timezone.now()
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RetrieveUserAPIView(RetrieveAPIView):
    serializer_class = BuddyProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        obj = BuddyProfile.objects.get(user=self.request.user )
        self.check_object_permissions(self.request, obj)
        return obj

class CreateIserAPIView(CreateAPIView):
    serializer_class = BuddyProfileSerializer
    permission_classes = [IsAuthenticated]
