from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserAuthSerializer(serializers.Serializer):

    class Meta:
        model = User
        fields = (
            'username',
            'password',
        )

    def validate_username(self, value):
        if not User.objects.filter(username=value).exists():
            raise serializers.ValidationError("존재하지 않는 아이디 입니다.")

        return value

