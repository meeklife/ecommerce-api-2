from rest_framework import serializers

from apps.users.models import User

from .models import Invitation


class InvitationSerializer(serializers.ModelSerializer):
    # A read-only field to represent the name of the inviter
    # This will include the name of the inviter in the serialized representation of the Invitation object.
    inviter = serializers.ReadOnlyField(source="inviter.username")
    referral_code = serializers.SerializerMethodField()

    class Meta:
        model = Invitation
        fields = [
            "id",
            "inviter",
            "referral_code",
            "email",
            "join",
        ]

    def get_referral_code(self, obj):
        return obj.inviter.username

    def validate_email(self, value):
        # Check if the email is already registered or an invitation is pending
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "This email is already registered on the platform."
            )  # used the validationError from Serializers
        elif Invitation.objects.filter(email=value, join=False).exists():
            raise serializers.ValidationError(
                "An invitation has already been sent to this email."
            )
        return value

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except Exception as e:
            raise serializers.ValidationError(f"Failed to create invitation: {str(e)}")
