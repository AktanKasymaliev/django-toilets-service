from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import *

urlpatterns = [
    path('toilet/list/', ToiletsPointListView.as_view(), name='toilets_list'),
    path('toilet/detail/<int:pk>/', ToiletsPointDetailView.as_view(), name='toilets_detail'),
    path('toilet/create/', ToiletsPointCreateView.as_view(), name='toilets_create'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


