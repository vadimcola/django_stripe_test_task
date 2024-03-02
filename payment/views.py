from rest_framework import generics
from django.views.generic import DetailView
from payment.models import Order
from payment.utils import get_total_order, get_payment_link
from payment.serializers import OrderSerializer


class OrderDetail(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_payment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total = get_total_order(self.object)
        payment_link = get_payment_link(self.object)
        context['total'] = total
        context['payment_link'] = payment_link
        return context
