from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site

def send_custom_email(mail_type:str, email_subject:str, template_path:str, user:object, email:str, request:object=None):

    if mail_type=='register':
        currentSite = settings.CURRENT_DOMAIN
    elif mail_type=='reset_pass':
        currentSite = get_current_site(request)

    mail_subject = email_subject
    message = render_to_string(template_path, {
        "user": user,
        "domain": currentSite,
        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
        "token": default_token_generator.make_token(user)
        })
    emailReceiver = email
    emialSender = settings.DEFAULT_FROM_EMAIL
    send_email= EmailMessage(mail_subject, 
                            message,
                            emialSender, 
                            to=[emailReceiver])
    
    send_email.send()