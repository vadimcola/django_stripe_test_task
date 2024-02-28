import stripe
from rest_framework import serializers

from config.settings import STRIPE_API_KEY
from payment.models import Order


class OrderSerializer(serializers.ModelSerializer):
    total_order = serializers.SerializerMethodField()
    payment_link = serializers.SerializerMethodField()

    def get_total_order(self, obj):
        total_price = sum(item.price for item in obj.items.all())

        if obj.discount:
            total_price -= (obj.discount.amount / 100) * total_price

        if obj.tax:
            total_price += (obj.tax.amount / 100) * total_price

        return total_price

    def get_payment_link(self, obj):
        stripe.api_key = STRIPE_API_KEY
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'rub',
                    'product_data': {
                        'name': 'Order {}'.format(obj.id),
                    },
                    'unit_amount': int(self.get_total_order(obj) * 100),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='https://example.com/success',
            cancel_url='https://example.com/cancel',
        )
        return session.url

    class Meta:
        model = Order
        fields = '__all__'
