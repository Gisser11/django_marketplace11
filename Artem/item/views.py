from django.shortcuts import render, get_object_or_404

from Artem.item.models import Item


def detail(request, PRIMARY_KEY):
    item = get_object_or_404(Item, PRIMARY_KEY=PRIMARY_KEY)

    return render(request, 'item/detail.html',{
        item:item
    })

# Create your views here.
