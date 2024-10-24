from rest_framework import generics, status
from rest_framework.generics import RetrieveAPIView, ListAPIView
from yaml import serialize

from buddy_groups.models import BuddyGroup, GroupAdmins, GroupMembers
from buddy_groups.serializers import BuddyGroupSerializer, BuddyGroupRequestSerializer, BuddyGroupRetrieveRequestSerializer
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from django.utils import timezone
from rest_framework.response import Response
import logging

from buddy_profiles.models import BuddyProfile


class BuddyGroupListCreateView(generics.ListCreateAPIView):
    queryset = BuddyGroup.objects.all()
    serializer_class = BuddyGroupSerializer
    permission_classes = [IsAuthenticated]

    logger = logging.getLogger('django')

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['group_members'] = self.request.data.get('group_members')
        context['group_admins'] = self.request.data.get('group_admins')
        return context

    @extend_schema(
        request=BuddyGroupRequestSerializer,
        responses={201: BuddyGroupSerializer}
    )
    def post(self, request, *args, **kwargs):
        # self.logger.info("Data from view"+ str(request.user))
        #
        return super().post(request, *args, **kwargs)

class BuddyGroupRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BuddyGroup.objects.all()
    serializer_class = BuddyGroupSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['group_members'] = self.request.data.get('group_members')
        context['group_admins'] = self.request.data.get('group_admins')
        return context

    @extend_schema(
        request=BuddyGroupRequestSerializer,
        responses={200: BuddyGroupSerializer}
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        request=BuddyGroupRequestSerializer,
        responses={200: BuddyGroupSerializer}
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    def perform_destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.deleted_date = timezone.now()
        instance.save()

        group_admins  = GroupAdmins.objects.filter(group_belong_to=instance)
        for admin_s in group_admins:
            admin_s.is_active = False
            admin_s.deleted_date = timezone.now()
            admin_s.save()

        group_members = GroupMembers.objects.filter(group_belong_to=instance)
        for member_s in group_members:
            member_s.is_active = False
            member_s.deleted_date = timezone.now()
            member_s.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

class RetrieveGroupAPIView(RetrieveAPIView):
    serializer_class = BuddyGroupRetrieveRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user_authenticated = BuddyProfile.objects.get(user=self.request.user)
        group_members = BuddyGroup.objects.filter(groupmembers__buddy_profile_member=user_authenticated)
        group_admins = BuddyGroup.objects.filter(groupadmins__buddy_profile_admin=user_authenticated)
        obj =  {'groups_that_belong':group_members, 'groups_that_manage':group_admins}
        # self.check_object_permissions(self.request, obj)
        return obj

    def retrieve(self, request, *args, **kwargs):
        # Get the model instance
        queryset = self.get_object()

        # Instantiate the serializer
        serializer = self.get_serializer(queryset, context={'request': request})

        # serializer = BuddyGroupRetrieveRequestSerializer(queryset, context={'request': request})

        # Return the serialized data
        return Response(serializer.data)

