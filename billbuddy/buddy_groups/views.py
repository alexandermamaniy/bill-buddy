from rest_framework import generics
from buddy_groups.models import BuddyGroup
from buddy_groups.serializers import BuddyGroupSerializer, BuddyGroupRequestSerializer
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema


class BuddyGroupListCreateView(generics.ListCreateAPIView):
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
        responses={201: BuddyGroupSerializer}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class BuddyGroupRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BuddyGroup.objects.all()
    serializer_class = BuddyGroupSerializer
    permission_classes = [IsAuthenticated]
