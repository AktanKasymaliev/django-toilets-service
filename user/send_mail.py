from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site



def send_confirmation_email(request, user):
    context = {
        "small_text_detail": "Thank you for "
        "creating an account. "
        "Please verify your email "
        "address to set up your account.",
        "email": user.email,
        "domain":get_current_site(request)
        # 'activation_code': user.activation_code
    }
    msg_html = render_to_string("account/email.html", context)
    plain_message = strip_tags(msg_html)
    subject = "Account activation"
    to_emails = user.email
    mail.send_mail(
        subject,
        plain_message,
        "akttan04@gmail.com",
        [to_emails, ],
        html_message=msg_html,
    )