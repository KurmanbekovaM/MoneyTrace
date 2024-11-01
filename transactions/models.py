from django.db import models

class Transaction(models.Model):
    TYPE_CHOICES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]
    transaction_type = models.CharField(max_length=7, choices=TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.transaction_type} - {self.amount}'


from django.contrib.auth.models import User 

# class Category(models.Model):
#     name = models.CharField(max_length=100)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="categories")

#     def __str__(self):
#         return self.name
class Category(models.Model):
    TYPE_CHOICES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]
    name = models.CharField(max_length=100)
    category_type = models.CharField(max_length=7, choices=TYPE_CHOICES, default='expense')  # Значение по умолчанию
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="categories")

    def __str__(self):
        return self.name



class Budget(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="budgets")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.category.name} - {self.amount}"

class ScheduledPayment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="scheduled_payments")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    scheduled_date = models.DateField()

    def __str__(self):
        return f"{self.amount} on {self.scheduled_date}"