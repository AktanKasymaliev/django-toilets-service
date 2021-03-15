from django.shortcuts import render
from .serializers import RegisterSerializer
from rest_framework import generics, viewsets, views, response, status
from .send_mail import send_confirmation_email






class RegisterView(views.View):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if not serializer.is_valid():
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        user = serializer.save()
        user.is_active = False
        user.save()
        current_site = get_current_site(request)
        mail_subject = 'Active your account'
        to_email = user.email
        message = render_to_string('templates/account/email.html', 
                                    {
                                        'user': user,
                                        'domain': current_site.domain,
                                        'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                                        'token': account_activation_token.make_token(user)
                                    })
        email = EmailMultiAlternatives(
            mail_subject,
            message,
            to = [user.email],
        )
        email.content_subtype = 'html'
        email.send(fail_silently=True)
        return response.Response('Email was send for confirmation',
                                status=status.HTTP_200_OK)
                        