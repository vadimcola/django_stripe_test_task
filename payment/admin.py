from django.contrib import admin

from payment.models import Item, Order, Discount, Tax


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_discount')


@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_tax')
