from buddy_groups.models import BuddyGroup
from rest_framework.serializers import ModelSerializer

class BuddyProfileSerializer(ModelSerializer):

    # group_members = GroupMembersSerializer()
    # group_admins = GroupAdminsSerializer()

    class Meta:
        model = BuddyGroup
        # fields = ['album_name', 'artist', 'tracks']
        exclude = ('created_date', 'modified_date', 'delete_date',)
