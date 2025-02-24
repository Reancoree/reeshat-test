from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from items.models import Item, Order
from project import settings
import stripe


def item_detail(request, id):
    item = get_object_or_404(Item, id=id)
    return render(request, 'shop/item_detail.html', {
        'item': item,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY
    })


def create_session(request, id):
    item = get_object_or_404(Item, id=id)
    stripe.api_key = settings.STRIPE_SECRET_KEY

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': item.currency,
                'product_data': {'name': item.name},
                'unit_amount': int(item.price * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:8000/success',
        cancel_url='http://localhost:8000/cancel',
    )
    return JsonResponse({'id': session.id})


def create_session_order(request, id):
    """Без проверки на одинаковые валюты.
    Возвращает json - нужна страница с переходом"""
    order = get_object_or_404(Order, id=id)
    stripe.api_key = settings.STRIPE_SECRET_KEY


    line_items = []
    for item in order.items.all():
        line_items.append({
            'price_data': {
                'currency': item.currency,
                'product_data': {'name': item.name},
                'unit_amount': int(item.price * 100),
            },
            'quantity': 1,
        })

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=line_items,
        mode='payment',
        success_url='http://localhost:8000/success',
        cancel_url='http://localhost:8000/cancel',
    )
    return JsonResponse({'id': session.id})
