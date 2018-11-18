from django.contrib.auth import get_user_model
from rest_framework import generics

from ..serializers import UserSignupSerializer

User = get_user_model()


class UserSignup(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSignupSerializer
