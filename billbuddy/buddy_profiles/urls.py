from django.urls import path
from buddy_profiles.views import BuddyProfileListCreateView, BuddyProfileRetrieveUpdateDestroy

urlpatterns = [
    path('buddy-profiles/', BuddyProfileListCreateView.as_view(), name='buddyprofile-list-create'),
    path('buddy-profiles/<uuid:pk>/', BuddyProfileRetrieveUpdateDestroy.as_view(), name='buddyprofile-detail'),
    # path('buddy-profiles/<uuid:pk>/', BuddyProfileRetrieveDestroyView.as_view(), name='buddyprofile-detail-destroy'),

    # path('buddy-profiles/<uuid:pk>/delete/', BuddyProfileDeleteView.as_view(), name='buddyprofile-delete'),
]
