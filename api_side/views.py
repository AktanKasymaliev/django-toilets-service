from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics, status, viewsets


from .models import Entity, AddressImage
from .serializers import *

class ToiletsPointListView(generics.ListAPIView):
    queryset = Entity.objects.all()
    serializer_class = ToiletsPointListSerialezer



class ToiletsPointDetailView(generics.RetrieveAPIView):
    queryset = Entity.objects.all()
    serializer_class = ToiletsPointsDetailSerializer


class ToiletsPointCreateView(generics.CreateAPIView):
    serializer_class = ToiletsPointCreateSerializer


class ToiletsPointDeleteView(generics.DestroyAPIView):
    serializer_class = ToiletsPointDeleteSerializera
    queryset = Entity.objects.all()
    

