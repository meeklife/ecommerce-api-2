from pathlib import Path

import environ
from django.core.mail import send_mail

BASE_DIR = Path(__file__).resolve().parent.parent.parent
APPS_DIR = BASE_DIR / "apps"
env = environ.Env()
env.read_env(str(BASE_DIR / ".env"))


def send_email(subject, message, recipient, fail_silently=False):
    send_mail(
        subject, message, env("FROM_EMAIL"), [recipient], fail_silently=fail_silently
    )
