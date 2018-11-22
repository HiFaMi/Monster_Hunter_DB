from django.contrib.auth import get_user_model

from ..backends.naver import NaverBackend

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from members.serializers.user import UserSerializer

__all__ = (
    'NaverAuth',
)

User = get_user_model()


class NaverAuth(APIView):

    def get(self, request):
        code = request.GET.get('code')
        user = NaverBackend.authenticate(request, code=code)

        token, __ = Token.objects.get_or_create(user=user)
        data = {
            'token': token.key,
            'user': UserSerializer(user).data,
        }

        return Response(data)
