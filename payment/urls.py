from django.urls import path

from payment.apps import PaymentConfig
from payment.views import OrderDetailView, OrderDetail

app_name = PaymentConfig.name

urlpatterns = [
    path('order/<int:pk>/', OrderDetailView.as_view(), name='detail'),
    path('buy/<int:pk>/', OrderDetail.as_view(), name='buy_id'),
]
