from rest_framework import generics

from payment.models import Order
from payment.serializers import OrderSerializer


class OrderDetail(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


