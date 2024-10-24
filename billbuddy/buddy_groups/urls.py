from django.urls import path
from .views import (
    BuddyGroupListCreateView,
    BuddyGroupRetrieveUpdateDestroyView, RetrieveGroupAPIView,
)

urlpatterns = [
    path('buddy-groups/', BuddyGroupListCreateView.as_view(), name='buddy-group-list-create'),
    path('buddy-groups/me', RetrieveGroupAPIView.as_view(), name='buddy-group-list-me'),
    path('buddy-groups/<uuid:pk>/', BuddyGroupRetrieveUpdateDestroyView.as_view(), name='buddy-group-detail'),
]