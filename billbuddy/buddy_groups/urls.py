from django.urls import path
from .views import (
    BuddyGroupListCreateView,
    BuddyGroupRetrieveUpdateDestroyView,
    # GroupMembersListCreateView,
    # GroupMembersRetrieveUpdateDestroyView,
    # GroupAdminsListCreateView,
    # GroupAdminsRetrieveUpdateDestroyView
)

urlpatterns = [
    path('buddy-groups/', BuddyGroupListCreateView.as_view(), name='buddy-group-list-create'),
    path('buddy-groups/<uuid:pk>/', BuddyGroupRetrieveUpdateDestroyView.as_view(), name='buddy-group-detail'),
]