from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Budget, ScheduledPayment, Transaction

admin.site.register(Category)
admin.site.register(Budget)
admin.site.register(ScheduledPayment)
admin.site.register(Transaction)
