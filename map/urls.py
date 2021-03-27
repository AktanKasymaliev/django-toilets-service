from django.urls import path
from .views import serializing, new_point, validating


urlpatterns = [
    path('', serializing, name='serialize'),
    path('new_point/', new_point, name='new_point'),
    path('validating/', validating, name='validating'),
]
