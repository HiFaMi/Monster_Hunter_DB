import requests
import json

from django.conf import settings
from django.contrib.auth import get_user_model, authenticate
from django.shortcuts import render

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
        user = authenticate(request, code=code)

        token, __ = Token.objects.get_or_create(user=user)
        data = {
            'token': token.key,
            'user': UserSerializer(user).data,
        }

        return Response(data)
