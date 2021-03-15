from django.template.loader import render_to_string
from .serializers import RegisterSerializer
from rest_framework import generics, viewsets, views, response, status
from .send_mail import send_confirmation_email
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, renderer_classes
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMultiAlternatives
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from user.models import User
from .token import account_activation_token



@api_view(['POST'])
@renderer_classes([JSONRenderer])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if not serializer.is_valid():
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    user = serializer.save()
    user.is_active = False
    user.save()
    send_confirmation_email(request, user)
    return response.Response('Email was send for confirmation',
                            status=status.HTTP_200_OK)

@api_view(['POST', 'GET'])
@renderer_classes([JSONRenderer])
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return response.Response('Your account activated')
    else:
        return response.Response('Error 404')
    