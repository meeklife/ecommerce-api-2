from django.core.mail import send_mail
from config.settings.base import env


def send_email(subject, message, recipient, fail_silently=False):
    send_mail(
        subject, message, env("FROM_EMAIL"), [recipient], fail_silently=fail_silently
    )
