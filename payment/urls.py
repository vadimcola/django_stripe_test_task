from django.urls import path

from payment.apps import PaymentConfig
from payment.views import OrderDetail

app_name = PaymentConfig.name

urlpatterns = [
    path('order/<int:pk>/', OrderDetail.as_view(), name='detail'),
]
