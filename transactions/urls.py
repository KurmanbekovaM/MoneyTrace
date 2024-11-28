from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransactionViewSet, CategoryViewSet, BudgetViewSet, ScheduledPaymentViewSet

router = DefaultRouter()
router.register(r'transactions', TransactionViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'budgets', BudgetViewSet)
router.register(r'scheduledpayments', ScheduledPaymentViewSet)

#urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
]



