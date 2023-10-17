import secrets
from django.urls import reverse
from django.core.mail import send_mail
from django.http import HttpRequest
from django.contrib.auth import login
from . import models


# http://localhost:8000/reset-password-by-email/?token=genered_token

def generate_token() -> str:
    new_token = secrets.token_hex(32)
    return new_token

def link_token_to_profile(profile:models.UserProfile):
    token = generate_token()
    profile.reset_token = token
    profile.save()

def send_reset_password_link(request:HttpRequest, profile:models.UserProfile):
    with open('accounts/templates/accounts/email_password_reset.html', 'r', encoding='utf-8') as file:
        message_content = file.read()
        message_content = message_content.replace('HREF', request.build_absolute_uri(reverse('accounts:password_reset_done', kwargs={'reset_token':profile.reset_token})))
        send_mail(subject='Смена пароля', message='Смена пароля', html_message=message_content, from_email='forstudy546@gmail.com', recipient_list=[profile.email])

def update_password_and_login(request:HttpRequest, profile:models.UserProfile, new_password:str):
    user = profile.user
    user.set_password(new_password)
    profile.password = new_password
    profile.save()
    user.save()
    login(request, user)

def update_profile(profile:models.UserProfile, data:dict) -> None:
    profile.name = data['name']
    profile.surname = data['surname']
    profile.age = data['age']
    profile.phone_number = data['phone_number']
    profile.save()
