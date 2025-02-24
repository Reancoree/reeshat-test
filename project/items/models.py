from django.db import models


class Item(models.Model):
    CURRENCY_CHOICES = [('usd', 'USD'), ('eur', 'EUR')]

    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='usd', verbose_name='Валюта')
    name = models.CharField(max_length=100, verbose_name='Имя')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return self.name


class Order(models.Model):
    items = models.ManyToManyField(Item)
