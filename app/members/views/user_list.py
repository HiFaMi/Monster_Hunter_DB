from django.contrib.auth import get_user_model
from rest_framework import generics

from members.serializers import UserSerializer

__all__ = (
    'UserList',
)

User = get_user_model()


class UserList(generics.ListAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
