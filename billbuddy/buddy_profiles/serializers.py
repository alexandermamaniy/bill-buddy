from buddy_profiles.models import BuddyProfile
from rest_framework.serializers import ModelSerializer
from users.serializers import UserSerializer
class BuddyProfileSerializer(ModelSerializer):

    user = UserSerializer()
    class Meta:
        model = BuddyProfile
        exclude = ('created_date', 'modified_date', 'delete_date',)