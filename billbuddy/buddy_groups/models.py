from django.db import models
import uuid
from buddy_profiles.models import BuddyProfile
from django.utils import timezone

class BuddyGroup(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('Group name', max_length=255, blank=False, null=False)

    group_members = models.ManyToManyField(BuddyProfile, through="GroupMembers", related_name='group_members')
    group_admins = models.ManyToManyField(BuddyProfile, through="GroupAdmins", related_name='group_admins')

    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(auto_now=True)
    deleted_date = models.DateTimeField('Deleted date', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

class GroupMembers(models.Model):
    buddy_profile_member = models.ForeignKey(BuddyProfile, on_delete=models.CASCADE)
    group_belong_to = models.ForeignKey(BuddyGroup, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(auto_now=True)
    deleted_date = models.DateTimeField('Deleted date', null=True, blank=True)
    is_active = models.BooleanField(default=True)


def __str__(self):
        return f'{self.buddy_profile_member.full_name} - {self.group_belong_to.name} '

class GroupAdmins(models.Model):
    buddy_profile_admin = models.ForeignKey(BuddyProfile, on_delete=models.CASCADE)
    group_belong_to = models.ForeignKey(BuddyGroup, on_delete=models.CASCADE)
    is_admin_a_member = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(auto_now=True)
    deleted_date = models.DateTimeField('Deleted date', null=True, blank=True)
    is_active = models.BooleanField(default=True)

