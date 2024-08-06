from django.urls import path
from buddy_profiles.views import BuddyProfileListCreateView, BuddyProfileRetrieveUpdateDestroyView

urlpatterns = [
    path('buddy-profiles/', BuddyProfileListCreateView.as_view(), name='buddyprofile-list-create'),
    path('buddy-profiles/<uuid:pk>/', BuddyProfileRetrieveUpdateDestroyView.as_view(), name='buddyprofile-detail'),
]
