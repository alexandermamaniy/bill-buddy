from rest_framework import generics
from buddy_profiles.models import BuddyProfile
from buddy_profiles.serializers import BuddyProfileSerializer
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import status

class BuddyProfileListCreateView(generics.ListCreateAPIView):
    queryset = BuddyProfile.objects.all()
    serializer_class = BuddyProfileSerializer

class BuddyProfileRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BuddyProfile.objects.all()
    serializer_class = BuddyProfileSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.deleted_date = timezone.now()
        instance.save()

        # Also set is_active to False for associated User
        user = instance.user
        user.is_active = False
        user.deleted_date = timezone.now()
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class BuddyProfileDeleteView(generics.DestroyAPIView):
#     queryset = BuddyProfile.objects.all()
#     serializer_class = BuddyProfileSerializer
#     # permission_classes = [IsAuthenticated]
#
#     def perform_destroy(self, instance):
#         # Set is_active to False for BuddyProfile
#         instance.is_active = False
#         instance.deleted_date = timezone.now()
#         instance.save()
#
#         # Also set is_active to False for associated User
#         user = instance.user
#         user.is_active = False
#         user.deleted_date = timezone.now()
#         user.save()