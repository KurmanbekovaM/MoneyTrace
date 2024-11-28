from rest_framework import viewsets
from .models import Transaction, Category, Budget, ScheduledPayment
from .serializers import TransactionSerializer, CategorySerializer, BudgetSerializer, ScheduledPaymentSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

class ScheduledPaymentViewSet(viewsets.ModelViewSet):
    queryset = ScheduledPayment.objects.all()
    serializer_class = ScheduledPaymentSerializer
