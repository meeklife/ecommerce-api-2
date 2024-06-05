from rest_framework import serializers

from .models import Invitation

from django.core.exceptions import ValidationError

from apps.users.models import User 

class InvitationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitation
        fields = [
            "id",
            "inviter",
            "referral_code",
            "email",
            "join",
        ]

    def validate_email(self, value):
        # Check if the email is already registered or an invitation is pending
        if User.objects.filter(email=value).exists():
            raise ValidationError("This email is already registered on the platform.")
        elif Invitation.objects.filter(email=value, join=False).exists():
            raise ValidationError("An invitation has already been sent to this email.")
        return value

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except ValidationError as e:
            raise serializers.ValidationError({"email": [str(e)]})
        except Exception as e:
            raise serializers.ValidationError(f"Failed to create invitation: {str(e)}")
