from rest_framework import generics, status
from rest_framework.generics import ListAPIView
from django.db.models import Q

from buddy_expenses.models import BuddyExpense
from buddy_expenses.serializers import BuddyExpenseSerializer, BuddyExpensesListSerializer
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

from buddy_profiles.models import BuddyProfile


class BuddyExpenseListCreateView(generics.ListCreateAPIView):
    queryset = BuddyExpense.objects.all()
    serializer_class = BuddyExpenseSerializer
    permission_classes = [IsAuthenticated]


    @extend_schema(
        request=BuddyExpenseSerializer,
        responses={201: BuddyExpenseSerializer}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class BuddyExpenseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BuddyExpense.objects.all()
    serializer_class = BuddyExpenseSerializer
    permission_classes = [IsAuthenticated]


    @extend_schema(
        request=BuddyExpenseSerializer,
        responses={200: BuddyExpenseSerializer}
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(
        request=BuddyExpenseSerializer,
        responses={200: BuddyExpenseSerializer}
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.deleted_date = timezone.now()
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BuddyExpensesOfOneProfileListAPIView(ListAPIView):
    serializer_class = BuddyExpensesListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_authenticated = BuddyProfile.objects.get(user=self.request.user)
        expenses = BuddyExpense.objects.filter(Q(participants_of_expense_payment=user_authenticated) | Q(payments_made_it_by_payers=user_authenticated))
        return {'expenses': expenses}

    def list(self, request, *args, **kwargs):
        # Get the queryset
        queryset = self.get_queryset()

        # Instantiate the serializer
        serializer = self.get_serializer(queryset, many=True)

        # Return the serialized data
        return Response(serializer.data)
    # Expense por group_id
    # BuddyExpense.objects.filter(buddy_group_id="dd904a5a-7718-4f05-bc57-9531c218f918")


class BuddyExpensesOfOneGroupListAPIView(ListAPIView):
    serializer_class = BuddyExpensesListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # user_authenticated = BuddyProfile.objects.get(user=self.request.user)
        
        # replace for Group id
        expenses = BuddyExpense.objects.filter(buddy_group_id="dd904a5a-7718-4f05-bc57-9531c218f918")
        return {'expenses': expenses}

    def list(self, request, *args, **kwargs):
        # Get the queryset
        queryset = self.get_queryset()

        # Instantiate the serializer
        serializer = self.get_serializer(queryset, many=True)

        # Return the serialized data
        return Response(serializer.data)

