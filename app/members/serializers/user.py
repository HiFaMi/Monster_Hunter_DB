from django.contrib.auth import get_user_model
from rest_framework import serializers

__all__ = (
    'UserSerializer',
)

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'create_at',
        )
