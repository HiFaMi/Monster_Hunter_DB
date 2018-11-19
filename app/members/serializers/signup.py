from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework import serializers
from ..tokens import account_activation_token

User = get_user_model()


class UserSignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
        )

    def validated_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("비밀번호는 8글자 이상이여야 합니다.")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            password=self.validated_data['password']
        )
        # user.save()
        # send_mail.delay(user.pk)

        message = render_to_string('account_activate_email.html', {
            'user': user,
            'domain': 'localhost:8000',
            'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode('utf-8'),
            'token': account_activation_token.make_token(user)
        })

        mail_subject = 'test'
        to_email = user.email
        email = EmailMessage(mail_subject, message, to=[to_email])
        email.send()

        return validated_data
