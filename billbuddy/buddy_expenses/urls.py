from django.urls import path
from .views import (BuddyExpenseListCreateView, BuddyExpenseRetrieveUpdateDestroyView,
                    BuddyExpensesOfOneProfileListAPIView, BuddyExpensesOfOneGroupListAPIView,
                    CreateExpenseOfUserAuthenticated)

urlpatterns = [
    # path('buddy-expenses/', BuddyExpenseListCreateView.as_view(), name='buddy-expense-list-create'),
    # path('buddy-expenses/<uuid:pk>/', BuddyExpenseRetrieveUpdateDestroyView.as_view(), name='buddy-expense-detail'),

    path('buddy-expenses/me', BuddyExpensesOfOneProfileListAPIView.as_view(), name='buddy-expenses-profile'),
    path('buddy-expenses/group/<uuid:pk>', BuddyExpensesOfOneGroupListAPIView.as_view(), name='buddy-expenses-group'),
    path('buddy-expenses/', CreateExpenseOfUserAuthenticated.as_view(), name='buddy-expenses-create'),



]

# BuddyExpensesOfOneProfileListAPIView