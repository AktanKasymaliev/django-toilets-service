from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import serializing, new_point


urlpatterns = [
    path('', serializing, name='serialize'),
    path('new_point/', new_point, name='new_point'),
]