from rest_framework import serializers
from .models import Transaction, Category, Budget, ScheduledPayment

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'transaction_type', 'amount', 'description', 'date']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'category_type', 'user']

class BudgetSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Budget
        fields = ['id', 'category', 'amount', 'start_date', 'end_date']

class ScheduledPaymentSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = ScheduledPayment
        fields = ['id', 'user', 'category', 'amount', 'scheduled_date']
