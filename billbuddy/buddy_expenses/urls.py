from django.urls import path
from .views import (BuddyExpenseListCreateView, BuddyExpenseRetrieveUpdateDestroyView)

urlpatterns = [
    path('buddy-expenses/', BuddyExpenseListCreateView.as_view(), name='buddy-group-list-create'),
    path('buddy-expenses/<uuid:pk>/', BuddyExpenseRetrieveUpdateDestroyView.as_view(), name='buddy-group-detail'),
]