from django.shortcuts import render
from api_side.models import Entity, Comment, AddressImage
from django.core import serializers



def serializing(request):
    context = {
        'queryset':Entity.objects.all(),
        'ents': serializers.serialize("json", Entity.objects.all())
    }
    return render(request, 'map/index.html', context)


def new_point(request):
    context = {
        'entity':Entity.objects.all(),
        'ents': serializers.serialize("json", Entity.objects.all())
    }
    return render(request, 'map/new_point.html', context)
