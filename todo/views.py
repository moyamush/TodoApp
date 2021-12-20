from django.shortcuts import render

from django.core.mail.backends import console
from django.http import HttpResponse
from django.core.mail import (
    send_mail, send_mass_mail, mail_admins, mail_managers, EmailMessage, EmailMultiAlternatives)
from django.conf import settings

from . import mail_schedule
from .api.views import CurrentUserAPIView

# def display_mail(request):
#     print("task: ",request.user.user_task)
#     print("django-request: ", request)
#     subject = ' タイトル '
#     message = f"{request.user}"
#     from_email = 'moyashi0324@gmail.com'
#     to = [request.user.email]
#     a = 10
#     b = 20
#     if a > b:
#         send_mail(subject, message, from_email, to)
        
#     return HttpResponse("success") 
