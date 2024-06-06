from rest_framework import serializers
from .models import Invitation
from apps.users.models import User 

class InvitationSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="inviter.name")

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
            raise serializers.ValidationError("This email is already registered on the platform.")
        elif Invitation.objects.filter(email=value, join=False).exists():
            raise serializers.ValidationError("An invitation has already been sent to this email.")
        return value

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except serializers.ValidationError as e:
            raise serializers.ValidationError({"email": [str(e)]})
        except Exception as e:
            raise serializers.ValidationError(f"Failed to create invitation: {str(e)}")
