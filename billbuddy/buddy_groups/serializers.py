from venv import logger
from rest_framework import serializers

from buddy_groups.models import BuddyGroup, GroupMembers, GroupAdmins
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from buddy_profiles.models import BuddyProfile
import logging

class GroupMembersSerializer(ModelSerializer):
    class Meta:
        model = GroupMembers
        fields = ['buddy_profile_member', 'group_belong_to']

class GroupAdminsSerializer(ModelSerializer):
    class Meta:
        model = GroupAdmins
        fields = ['buddy_profile_admin', 'group_belong_to', 'is_admin_a_member']

class BuddyGroupRequestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255, help_text='Name of the buddy group')
    group_members = serializers.ListField(
        child=serializers.UUIDField(format='hex_verbose'),
        help_text='List of member IDs'
    )
    group_admins = serializers.ListField(
        child=serializers.UUIDField(format='hex_verbose'),
        help_text='List of admin IDs'
    )



class BuddyGroupSerializer(ModelSerializer):
    group_members = GroupMembersSerializer(source='groupmembers_set', many=True, read_only=True)
    group_admins = GroupAdminsSerializer(source='groupadmins_set', many=True, read_only=True)

    logger = logging.getLogger('django')

    class Meta:
        model = BuddyGroup
        fields = ['id', 'name', 'group_members', 'group_admins']

    def create(self, validated_data):
        group_members_data = self.context.get('group_members')
        group_admins_data = self.context.get('group_admins')

        buddy_group = BuddyGroup.objects.create(**validated_data)

        for member_data in group_members_data:
            buddy_profile_member = BuddyProfile.objects.get(id=member_data)
            GroupMembers.objects.create(group_belong_to=buddy_group, buddy_profile_member=buddy_profile_member)

        for admin_data in group_admins_data:
            buddy_profile_admin = BuddyProfile.objects.get(id=admin_data)
            GroupAdmins.objects.create(group_belong_to=buddy_group, buddy_profile_admin=buddy_profile_admin)

        return buddy_group

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()

        group_members_data = self.context.get('group_members')
        group_admins_data = self.context.get('group_admins')

        if group_members_data is not None:
            instance.groupmembers_set.all().delete()
            for member_data in group_members_data:
                buddy_profile_member = BuddyProfile.objects.get(id=member_data)
                GroupMembers.objects.create(group_belong_to=instance, buddy_profile_member=buddy_profile_member)

        if group_admins_data is not None:
            instance.groupadmins_set.all().delete()
            for admin_data in group_admins_data:
                buddy_profile_admin = BuddyProfile.objects.get(id=admin_data)
                GroupAdmins.objects.create(group_belong_to=instance, buddy_profile_admin=buddy_profile_admin)

        return instance
