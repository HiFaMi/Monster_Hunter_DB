from django.contrib.auth import get_user_model

from ..backends.kakao import KakaoBackend

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from members.serializers.user import UserSerializer

__all__ = (
    'KakaoAuth',
)

User = get_user_model()


class KakaoAuth(APIView):

    def get(self, request):
        code = request.GET.get('code')
        user = KakaoBackend.authenticate(request, code=code)

        token, __ = Token.objects.get_or_create(user=user)
        data = {
            'token': token.key,
            'user': UserSerializer(user).data,
        }

        return Response(data)
