from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('image', AddressImageView)

urlpatterns = [
    # path('image/list/', AddressImageView.as_view(), name='images_list'),
    path('restroom/list/', ToiletsPointListView.as_view(), name='restroom_list'),
    path('restroom/detail/<int:pk>/', ToiletsPointDetailView.as_view(), name='restroom_detail'),
    path('restroom/create/', ToiletsPointCreateView.as_view(), name='restroom_create'),
    path('restroom/delete/<int:pk>/', ToiletsPointDeleteView.as_view(), name='restroom_delete'),
    path('restroom/update/<int:pk>/', ToiletsPointUpdateView.as_view(), name='restroom_update'),
    path('restroom/comments/', CommentView.as_view(), name='comment_list'),
    path('restroom/comment/add/', CommentCreateView.as_view(), name='comment_add'),
    path('restroom/comment/<int:pk>/', CommentCRUDView.as_view(), name='comment_crud')
    # path('restroom/comment/edit/<int:pk>/', CommentView.as_view(), name='comment_list')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += router.urls

