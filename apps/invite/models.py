from django.db import models

from apps.common import models as base_models

from apps.users.models import User

from apps.common import email

from django.dispatch import receiver

import logging



logger = logging.getLogger(__name__)



class Invitation(base_models.BaseModel):
    inviter = models.ForeignKey(User, on_delete=models.CASCADE)  # The user who is sending the invitation
    referral_code = models.CharField(max_length=50)
    email = models.EmailField()  # The email address of the invitee
    join = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Invitation from {self.inviter.username} to {self.email}"

# SIGNALS

@receiver(models.signals.post_save, sender=Invitation)
def send_invitation_email(sender, instance, created, **kwargs):
    if created:
        try:

            subject = "You've been invited to join our platform!"
            message = (
                f"Hi, you've been invited to join our platform by "
                f"{instance.inviter.username}! Use the referral code "
                f"{instance.referral_code} to sign up."
            )
            email.send_email(instance.email, subject, message)
        except Exception as e:
            logger.error(f"Error sending invitation email: {e}")
    
