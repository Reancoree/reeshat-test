from django.shortcuts import render, get_object_or_404

from items.models import Item
from project import settings


def item_detail(request, id):
    item = get_object_or_404(Item, id=id)
    return render(request, 'shop/item_detail.html', {
        'item': item,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY
    })
