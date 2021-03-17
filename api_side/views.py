from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import generics, status, viewsets
from rest_framework.permissions import (IsAuthenticated,AllowAny)
from rest_framework.decorators import api_view

from .paginations import Pagination
from .permissions import IsOwner, IsCommentOwnerOrPostAdmin, IsOwnerImage
from django.db.models import Q 
from .models import Entity, AddressImage, Comment
from .serializers import *



# Toilet points
# -----------------------------------------------------
class ToiletsPointListView(generics.ListAPIView):
    queryset = Entity.objects.all()
    serializer_class = ToiletsPointListSerialezer
    permission_classes = [AllowAny,]
    pagination_class = Pagination

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
    permission_classes = [AllowAny,]


class ToiletsPointCreateView(generics.CreateAPIView):
    serializer_class = ToiletsPointCreateSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class ToiletsPointDeleteView(generics.DestroyAPIView):
    serializer_class = ToiletsPointDeleteSerializer
    queryset = Entity.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

    
class ToiletsPointUpdateView(generics.UpdateAPIView):
    serializer_class = ToiletsPointUpdateSerializer
    queryset = Entity.objects.all()
    http_method_names = ['patch',]
    permission_classes = [IsAuthenticated, IsOwner]
# ----------------------------------------------------------------


# Address image
# -------------------------------------------------
class AddressImageView(generics.ListAPIView):
    serializer_class = AddressImageSerializer
    queryset = AddressImage.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerImage]
    pagination_class = Pagination

class AddressImageCreateView(generics.CreateAPIView):
    serializer_class = AddressImageCreateSerializer
    permission_classes = [IsAuthenticated, IsOwnerImage]

class AddressImageCRUDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AddressImageCRUDSerializer
    queryset = AddressImage.objects.all()
    permission_classes = [IsAuthenticated,]

    # def update(self, request, *args, **kwargs):
    #     updating = super(AddressImageCRUDView, self).update(request, *args, **kwargs) 
    #     updating.
    #     return updating

    def put(self, request, *args, **kwargs):
        return Response('Put method not allowed')
    
    def get(self, request, *args, **kwargs):
        return Response('Get method not allowed')
# -------------------------------------------------------


#Comments
# ---------------------------------------------
class CommentView(generics.ListAPIView):
    serializer_class = ComentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated,]
    pagination_class = Pagination

class CommentCreateView(generics.CreateAPIView):
    serializer_class = ComentCreateSerializer
    permission_classes = [IsAuthenticated,]

class CommentCRUDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ComentCRUDSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated,IsCommentOwnerOrPostAdmin]

    def get(self, request, *args, **kwargs):
        return Response('Get method not allowed')

    
#-----------------------------------------------------