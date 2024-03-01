import stripe

from config.settings import STRIPE_API_KEY


def get_total_order(obj):
    total_price = sum(item.price for item in obj.items.all())

    if obj.discount:
        total_price -= (obj.discount.amount / 100) * total_price

    if obj.tax:
        total_price += (obj.tax.amount / 100) * total_price

    return total_price


def get_payment_link(obj):
    stripe.api_key = STRIPE_API_KEY
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'rub',
                'product_data': {
                    'name': 'Order {}'.format(obj.id),
                },
                'unit_amount': int(get_total_order(obj) * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='https://example.com/success',
        cancel_url='https://example.com/cancel',
    )
    return session.url
