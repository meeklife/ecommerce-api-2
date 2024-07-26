from anymail.message import AnymailMessage
from django.core.mail import EmailMessage

from config.settings.base import env


def send_email(subject, message, recipient, fail_silently=False):
    msg = EmailMessage(
        subject,
        message,
        from_email=env("FROM_EMAIL"),
        to=[recipient],
        reply_to=[recipient],
    )

    return msg.send(fail_silently=fail_silently)


def send_email_template(
    email, template_id: str, dynamic_template_data: dict = None, fail_silently=True
):
    """
    Helper to send emails system wide.
    Special consideration made for sendgrid's dynamic templating.

    https://docs.sendgrid.com/ui/sending-email/how-to-send-an-email-with-dynamic-transactional-templates
    """
    msg = AnymailMessage(
        from_email=env("FROM_EMAIL"),
        to=[email],
        reply_to=[env("FROM_EMAIL")],
    )
    msg.template_id = template_id

    if dynamic_template_data:
        msg.merge_data = dynamic_template_data

    return msg.send(fail_silently=fail_silently)
