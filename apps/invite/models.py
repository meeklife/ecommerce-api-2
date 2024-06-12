from django.db import models

from apps.common import email
from apps.common import models as base_models
from apps.users.models import User


class Invitation(base_models.BaseModel):
    inviter = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # The user who is sending the invitation
    referral_code = models.CharField(max_length=50)
    email = models.EmailField()  # The email address of the invitee
    join = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Send email to the invitee
        subject = "You've been invited to join our platform!"
        message = f"Hi, you've been invited to join our platform by {self.inviter.username}! Use the referral code {self.referral_code} to sign up."
        email.send_email(subject, message, self.email)
        # email.send_email_template(self.email, "d-f695a7a6facd42c2ab77cd18db2c2363",
        #                           {"username": self.inviter.username, "referral_code": self.referral_code})

    def __str__(self):
        return f"Invitation from {self.inviter.username} to {self.email}"
