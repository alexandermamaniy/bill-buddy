from rest_framework import generics, status
from buddy_expenses.models import BuddyExpense
from buddy_expenses.serializers import BuddyExpenseSerializer
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

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