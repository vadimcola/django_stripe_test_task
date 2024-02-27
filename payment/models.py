from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Item(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование предмета')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


class Order(models.Model):
    items = models.ManyToManyField(Item, verbose_name='Наименование предмета')
    discount = models.ForeignKey('Discount', on_delete=models.SET_NULL, **NULLABLE, verbose_name='Скидка')
    tax = models.ForeignKey('Tax', on_delete=models.SET_NULL, **NULLABLE, verbose_name='Налог')

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплаты'


class Discount(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма скидки')

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'


class Tax(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма налога')

    class Meta:
        verbose_name = 'Налог'
        verbose_name_plural = 'Налоги'
