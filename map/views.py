from django.shortcuts import render
from api_side.models import Entity, Comment, AddressImage
from django.core import serializers



def serializing(request):
    context = {
        'user': request.user,
        'queryset': Entity.objects.all(),
        'ents': serializers.serialize("json", [x for x in Entity.objects.all() if x.has_published is not False])
    }
    return render(request, 'map/index.html', context)


def new_point(request):
    context = {
        'entity': Entity.objects.all(),
        'ents': serializers.serialize("json", [x for x in Entity.objects.all() if x.has_published is not False])
    }
    return render(request, 'map/new_point.html', context)


def validating(request):
    context = {
        'ent': serializers.serialize("json", Entity.objects.all())
    }
    return render(request, 'map/validate.html', context)
