from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics, status, viewsets


from django.db.models import Q 
from .models import Entity, AddressImage
from .serializers import *


class ToiletsPointListView(generics.ListAPIView):
    queryset = Entity.objects.all()
    serializer_class = ToiletsPointListSerialezer

    def get_queryset(self):
        search_ = self.request.query_params.get('search')
        my_queryset = super().get_queryset() 
        if search_:
            my_queryset = my_queryset.filter(address__icontains=search_)
            return my_queryset
        else:
            return my_queryset

class ToiletsPointDetailView(generics.RetrieveAPIView):
    queryset = Entity.objects.all()
    serializer_class = ToiletsPointsDetailSerializer


class ToiletsPointCreateView(generics.CreateAPIView):
    serializer_class = ToiletsPointCreateSerializer


class ToiletsPointDeleteView(generics.DestroyAPIView):
    serializer_class = ToiletsPointDeleteSerializer
    queryset = Entity.objects.all()
    
class ToiletsPointUpdateView(generics.UpdateAPIView):
    serializer_class = ToiletsPointUpdateSerializer
    queryset = Entity.objects.all()
    http_method_names = ['patch',]


class AddressImageView(viewsets.ModelViewSet):
    serializer_class = ToiletAddressImageSerializer
    queryset = AddressImage.objects.all()